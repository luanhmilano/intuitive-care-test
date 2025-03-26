from pathlib import Path
import zipfile
import pandas as pd
from ..utils.data_cleaner import clean_data 
from ..utils.extract_pdf_tables import extract_pdf_tables
from ..utils.validate_rol_data import validate_rol_data
from shared.logger import get_logger

logger = get_logger()

class ROLExtractionPipe:
    def __init__(self, output_name: str):
        self.output_name = output_name
        self.output_dir = Path('data/processed')
        self._ensure_output_dir()
    
    def _ensure_output_dir(self):
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def _save_output(self, df: pd.DataFrame) -> str:
        csv_path = self.output_dir / f"ROL_Processado_{self.output_name}.csv"
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        return csv_path

    def _create_zip(self, csv_path: Path) -> str:
        zip_path = self.output_dir / f"Teste_{self.output_name}.zip"
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(csv_path, arcname=csv_path.name)
        return zip_path
    
    def execute(self, pdf_path: str) -> str:
        """Fluxo completo ETL"""
        try:
            logger.info("Iniciando pipeline de transformação...")

            logger.debug("Extraindo tabelas do PDF...")
            try:
                tables = extract_pdf_tables(pdf_path)
            except Exception as e:
                logger.error(f"Falha na extração do PDF: {str(e)}")
                raise

            combined_df = pd.concat(tables, ignore_index=True)

            logger.debug(f"Colunas extraídas: {combined_df.columns.tolist()}")
            combined_df.to_csv("debug_raw_data.csv", index=False)

            cleaned_df = clean_data(combined_df)
            logger.debug(f"Colunas após limpeza: {cleaned_df.columns.tolist()}")
            cleaned_df.to_csv("debug_cleaned_data.csv", index=False)

            validated_df = validate_rol_data(cleaned_df)

            logger.debug("Gerando arquivos de saída...")
            csv_path = self._save_output(validated_df)
            zip_path = self._create_zip(csv_path)

            logger.info(f"Pipeline concluído: {zip_path}")
            return zip_path
        
        except Exception as e:
            logger.error(f"Falha na pipeline: {str(e)}")
            raise
