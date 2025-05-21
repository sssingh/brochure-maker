from typing import List, Tuple
from rich import print
from time import sleep
import nodriver as uc
from bs4 import BeautifulSoup


# scrape the passed url page
async def _scrape(url: str, links_required: bool) -> Tuple[str, List[str]]:
    print("[INFO]: Launching browser...")
    browser = await uc.start()
    print(f"[INFO]: Scraping page {url}...")
    page = await browser.get(url)
    sleep(3)
    home_page = await page.get_content()
    print("[INFO]: Parsing HTML...")
    soup = BeautifulSoup(markup=home_page, features="html.parser")
    text = soup.get_text()
    links = await page.get_all_urls() if links_required else []
    return text, links


# process single page
def get_page(url: str, links_required: bool) -> Tuple[str, List[str]]:
    return uc.loop().run_until_complete(_scrape(url, links_required))


# process the list of pages
def get_all_pages(urls: List[str]) -> str:
    print(urls)
    all_text = ""
    for url in urls[:10]:  # Limiting it to scrape only 10 pages
        page_text, _ = get_page(url=url, links_required=False)
        all_text += "\n" + page_text
    return all_text
