# Company Brochure Maker

> Given a company website URL the Brochure Maker will leverage the power of 
> `Large Language Model (LLM)` to scrape the details from home-page, decide
> which links on the page is relevant then scrape details from these links
> and then prepares a brochure based on gathered details for company's
> prospective customers, employees, suppliers and business partners.
> Brochure is displayed in markdown format and can be copied to clip board.
> Brochure can also be downloaded in `pdf` format.

🎥 Check out the [YouTube tutorial](https://youtu.be/WfNPbak-1mM) for a detailed discussion & step-by-step guide, and stay tuned for more GenAI projects! 🌐

## App High Level Design

![Abstract](/shared/readme-design.png)

## App Interface and Usage

![App Interface](/shared/app-usage.png "title")  

> scrapped raw data is saved in the `data` folder as `website_text.txt` & its 
> used as data-source for susequent runs. Delete this file generate brochure 
> again if re-scrapping is required.  

>Downloaded button will download the brochure in PDF & Markdown format, these
> files are also saved in `data` folder

## Installation and Run

* By default app uses `Azure` hosted `gpt-4o-mini`, If you are also using azure hosted model then create `.env` file and
  supply below details. An sample is provided in `.env_example`:
  AZURE_OPENAI_API_KEY 
  AZURE_OPENAI_ENDPOINT 
  AZURE_OPENAI_LLM_DEPLOYMENT_ID 
  AZURE_OPENAI_API_VERSION   

* If using OpenAI hosted model then:
  - create `.env` file and supply OPENAI_API_KEY .env, An sample is provided in `.env_example`
  - replace line 15 in `process.py` to ```python llm = lc.connect(host="openai", model=<openai-model-name>)```  

* If using Ollama running locally then:
  - replace line 15 in `process.py` to ```python llm = lc.connect(host="ollama", model=<ollama-model-name>)```  
  
>Since this app relies on models ability to reason, when using small open source model the output may not be
>as good as when using openai models.

```console
cd path/to/your/directory
git clone https://github.com/sssingh/brochure-maker.git
cd brochure-maker
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python app.py
[Open the shown localhost url in your browser]
```

