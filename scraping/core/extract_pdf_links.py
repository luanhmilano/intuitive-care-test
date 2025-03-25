from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import List

def extract_pdf_links(soup: BeautifulSoup, base_url: str) -> List[str]:
    """Extrai links PDF de uma página"""
    return [
        urljoin(base_url, a['href'])
        for a in soup.find_all('a', href=True)
        if a['href'].lower().endswith('.pdf')
    ][:2]