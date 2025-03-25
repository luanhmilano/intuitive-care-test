import os

def create_directory(path: str) -> None:
    """Cria um diretório se não existir"""
    os.makedirs(path, exist_ok=True)
    if not os.path.exists(path):
        raise IOError(f"Falha ao criar diretório: {path}")