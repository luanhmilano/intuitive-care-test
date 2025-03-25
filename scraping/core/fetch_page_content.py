import requests
from bs4 import BeautifulSoup

def fetch_page_content(url: str) -> BeautifulSoup:
    """Obtém e parseia o conteúdo HTML"""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.content, 'html.parser')