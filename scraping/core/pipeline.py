import os
import zipfile
import requests
from dotenv import load_dotenv
from typing import Optional
from ..utils.create_directory import create_directory
from ..utils.validate_url import validate_url
from ..utils.generate_zip_name import generate_zip_name
from .fetch_page_content import fetch_page_content
from .extract_pdf_links import extract_pdf_links

load_dotenv()

def download_pdfs_and_zip(url: Optional[str] = None, output_zip: Optional[str] = None) -> Optional[str]:
    """Função principal do módulo"""
    try:
        base_dir = os.path.abspath(os.path.dirname(__file__))
        zip_dir = os.path.join(base_dir, '../../data/raw')
        create_directory(zip_dir)

        target_url = url or os.getenv('TARGET_URL').removeprefix('"').removesuffix('"\'')
        if not target_url:
            raise ValueError('URL não configurada')
        validate_url(target_url)

        soup = fetch_page_content(target_url)
        pdf_links = extract_pdf_links(soup, target_url)

        if not pdf_links:
            raise ValueError("Nenhum PDF encontrado")
        
        zip_name = generate_zip_name(output_zip)
        zip_path = os.path.join(zip_dir, zip_name)

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for i, link in enumerate(pdf_links):
                pdf_response = requests.get(link, timeout=10)
                pdf_response.raise_for_status()
                zipf.writestr(f'arquivo_{i+1}.pdf', pdf_response.content)

        return zip_path
    except (requests.exceptions.RequestException, ValueError, IOError) as e:
        print(f"Erro: {str(e)}")
        return None