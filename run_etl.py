import zipfile
import os
from pathlib import Path
from datetime import datetime
from transformation.core.pipeline import ROLExtractionPipe
from shared.logger import get_logger

logger = get_logger()

def find_latest_scraping_zip() -> Path:
    """Encontra o ZIP mais recente gerado pelo scraping"""
    zip_dir = Path('data/raw')
    zip_files = list(zip_dir.glob('anexos_*.zip'))

    if not zip_files:
        raise FileNotFoundError("Nenhum arquivo ZIP encontrado")
    
    latest_zip = max(zip_files, key=os.path.getmtime)
    logger.info(f"Arquivo ZIP mais recente: {latest_zip}")
    return latest_zip

def extract_anexo_ii(zip_path: Path) -> Path:
    """Extrai o Anexo II do ZIP do scraping"""
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        for file_info in zipf.infolist():
            if 'arquivo_2' in file_info.filename and file_info.filename.endswith('.pdf'):
                output_dir = Path('data/raw')
                output_dir.mkdir(exist_ok=True)

                zipf.extract(file_info, output_dir)
                extracted_path = output_dir / file_info.filename
                logger.info(f"Arquivo extraído: {extracted_path}")
                return extracted_path
        raise FileNotFoundError(f"Anexo não encontrado no ZIP: {zip_path}")

def main(output_name: str = "luan-henrique-dos-santos-silva"):
    try:
        scraping_zip = find_latest_scraping_zip()

        pdf_path = extract_anexo_ii(scraping_zip)

        pipeline = ROLExtractionPipe(output_name)
        result_path = pipeline.execute(str(pdf_path))

        logger.info(f"Processo concluído com sucesso!\nArquivo final: {result_path}")
        return result_path
    
    except Exception as e:
        logger.error(f"Erro no processo do ETL: {str(e)}")
        raise

if __name__ == '__main__':
    main()
