def validate_url(url: str) -> None:
    """Validação básica de URL"""
    if not url.startswith(('http://', 'https://')):
        raise ValueError("URL inválida. Deve começar com http:// ou https://")