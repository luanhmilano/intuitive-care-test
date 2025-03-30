import os
import zipfile
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def parse_quarter(filename: str) -> str:
    """Extrai o período do nome do arquivo: 1T2023 -> 2023T1"""
    quarter, year = filename.split('T')
    return f"{year}T{quarter}"

def load_data():
    db_conn = os.getenv('DB_CONN')
    engine = create_engine(db_conn)

    for year in [2023, 2024]:
        for q in range(1, 5):
            zip_path = f"data/raw/demonstracoes_contabeis-{year}/{q}T{year}.zip"
            
            with zipfile.ZipFile(zip_path) as zf:
                with zf.open(f"{q}T{year}.csv") as f:
                    df = pd.read_csv(
                        f, 
                        sep=';', 
                        encoding='latin1',
                        parse_dates=['DATA'],
                        dtype={'REG_ANS': str, 'CD_CONTA_CONTABIL': str}
                    )
                    df['periodo'] = parse_quarter(f"{q}T{year}")
                    
                    df.to_sql(
                        'demonstracoes_contabeis',
                        engine,
                        if_exists='append',
                        index=False,
                        chunksize=1000
                    )
    
    df_operadoras = pd.read_csv(
        'data/raw/operadoras_ativas/Relatorio_cadop.csv',
        sep=';',
        encoding='latin1',
        dtype={'Registro_ANS': str, 'CNPJ': str}
    ).rename(columns={'Registro_ANS': 'registro_ans'})
    
    df_operadoras.to_sql(
        'operadoras',
        engine,
        if_exists='replace',
        index=False
    )