import pandas as pd
from ..schemas.rol_schema import ROL_SCHEMA

def validate_rol_data(df: pd.DataFrame) -> pd.DataFrame:
    """Valida os dados extraídos"""
    try:
        return ROL_SCHEMA.validate(df)
    except Exception as e:
        raise ValueError(f"Validação dos dados falhou: {str(e)}")