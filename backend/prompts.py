user_prompt_urls = """From home page {home_page_url} of a company named 
{company_name}, You have been given a list of urls below:\n\n{urls}\n\n. Reason 
through this list and keep only those urls that would be relevant for creating 
compnay's brochure for its prospective customers, suppliers and employees. 
Ignore links related with social media, site navigation, copyright, terms and 
conditions, legal and privacy. Do not include the home page url in the list.
Ensure all urls are absolute in the output
"""

system_prompt = """You are an expert in creating company brochure targetted 
towards prospective customers, suppliers and employees. For a company named 
{company_name} you have been provided a text corpus gathered from various pages
in its website. Generate a crisp, professional but catchy 
brochure to market company product, services & expertise. You will produce a 
markdown formatted output. Use bullets, emojis and tables where appropriate,
be reasonably verbose. do NOT annotate the begining of the output text 
indicating that its markdown format output."""

user_prompt_brochure = """here is the text: \n{text}"""
