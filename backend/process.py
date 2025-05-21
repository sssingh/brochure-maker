from rich import print
from pathlib import Path
from dotenv import load_dotenv
from backend import lc, prompts, schema, process
from shared import scraper, utils


load_dotenv()

DATA_TXT_FILE = "data/website_text.txt"
BROCHURE_MD_FILE = "data/brochure.md"
BROCHURE_PDF_FILE = "data/brochure.pdf"

# llm = lc.connect("azure")
llm = lc.connect(host="azure")
llm_structured_output = llm.with_structured_output(schema.RelevantUrls)
prompt_template_urls = lc.make_prompt_template(
    user_prompt=prompts.user_prompt_urls
)


def get_company_data(company_name, company_url, save_data: bool = True) -> str:
    # if data already prepared then use it, save LLM API call cost
    all_text = ""
    if Path(DATA_TXT_FILE).exists():
        try:
            print("[INFO]: Reading data from saved file...")
            with open(DATA_TXT_FILE, "r", encoding="utf-8") as f:
                all_text = f.read()
        except Exception as e:
            print(e)
    else:
        print("[INFO]: No saved data found, making LLM API calls...")
        # scrape home page, get text and links on the page
        home_page_text, urls_list = scraper.get_page(
            url=company_url, links_required=True
        )

        # keep only the relevant links
        print("[INFO]: LLM filtering out irrelevant urls...")
        prompt = prompt_template_urls.invoke(
            {
                "company_name": company_name,
                "home_page_url": company_url,
                "urls": urls_list,
            }
        )
        response = llm_structured_output.invoke(prompt)
        relevant_urls = response.relevant_urls

        # scrape all relevant links one by one and extract combined text
        link_text = scraper.get_all_pages(urls=relevant_urls)
        # combine it with home-page text, keep only first 20k char to save cost :)
        all_text = (
            "company-name: "
            + company_name
            + "\n"
            + home_page_text
            + "\n"
            + link_text
        )
        # save data to be used in next run
        if save_data:
            try:
                print("[INFO]: Saving data to a text file...")
                with open(DATA_TXT_FILE, "w", encoding="utf-8") as f:
                    f.write(all_text)
            except Exception as e:
                print(e)
    return all_text


def generate_brochure(company_name, company_url):
    # gather data from company's website
    text = process.get_company_data(
        company_name=company_name, company_url=company_url
    )

    print("[INFO]: LLM is generating Brochure...")
    # ask LLM to generate brochure
    prompt_template_urls = lc.make_prompt_template(
        system_prompt=prompts.system_prompt,
        user_prompt=prompts.user_prompt_brochure,
    )
    prompt = prompt_template_urls.invoke(
        {
            "company_name": company_name,
            "text": text[:20_000],
        }  # 20k chars only to save cost
    )
    response = llm.invoke(prompt)
    try:
        print("[INFO]: Saving brochure in markdown format...")
        with open(BROCHURE_MD_FILE, "w", encoding="utf-8") as f:
            f.write(response.content)
        print("[INFO]: Saving brochure in PDF format...")
        utils.save_md_as_pdf(
            md_path=BROCHURE_MD_FILE, pdf_path=BROCHURE_PDF_FILE
        )
        print("[INFO]: DONE!")
    except Exception as e:
        print(e)
    return response.content
