import pandas as pd

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Padroniza nomes das colunas removendo caracteres especiais"""
    df.columns = (
        df.columns.str.strip()
        .str.replace('\r', ' ')
        .str.replace('[^a-zA-Z0-9_]', '_', regex=True)
        .str.replace('__', '_', regex=False)
        .str.strip('_')
        .str.upper()
    )
    return df.rename(columns={
        'RN_ALTERACAO': 'RN',
        'UNNAMED_0': 'ID',
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    })

def drop_unnecessary_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Remove colunas indesejadas"""
    return df.drop(columns=['ID'], errors='ignore')

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Pipeline completo de limpeza"""
    df = clean_column_names(df)
    df = drop_unnecessary_columns(df)
    return df