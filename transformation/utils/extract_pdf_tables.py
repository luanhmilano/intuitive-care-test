import tabula
import pandas as pd
from typing import List

def extract_pdf_tables(pdf_path: str) -> List[pd.DataFrame]:
    """Extrai tabelas de PDFs usando tabula-py"""
    try:
        return tabula.read_pdf(
            pdf_path,
            pages="all",
            multiple_tables=True,
            lattice=True,
            area=[70, 0, 750, 590],
            pandas_options={'header': None},
            stream=True,
            encoding='utf-8',
            silent=True
        )
    except Exception as e:
        raise RuntimeError(f"PDF parsing error: {str(e)}")