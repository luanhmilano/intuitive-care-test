from typing import Optional, List
from datetime import datetime

def generate_zip_name(base_name: Optional[str] = None) -> str:
    """Gera um nome único para o arquivo ZIP"""
    if base_name is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"anexos_{timestamp}.zip"
    return base_name