from scraping.core.main import download_pdfs_and_zip
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    result = download_pdfs_and_zip()
    if result:
        print(f"Arquivo gerado: {result}")
    else:
        print("Falha na execução")