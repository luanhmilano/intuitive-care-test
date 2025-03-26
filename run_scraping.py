from scraping.core.pipeline import download_pdfs_and_zip
from shared.logger import get_logger

logger = get_logger()

def main():
    logger.info("Iniciando processo de scraping...")
    zip_path = download_pdfs_and_zip()
    if zip_path:
        print(f"Arquivo gerado: {zip_path}")
    else:
        print("Falha na execução")

if __name__ == "__main__":
    main()
