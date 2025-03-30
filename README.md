# Intuitive Care - Testes de Nivelamento v.250321

Testes realizados com a stack Python.\
Pipeline automatizado para processamento de dados de planos de saúde, incluindo (1) coleta de documentos e (2) transformação de dados.

## Funcionalidades Principais

- **Coleta Automática de PDFs**
  - Identificação de links de uma página do GOV
  - Download seguro de documentos (anexos)
  - Organização em arquivos ZIP datados

- **Processamento de Dados**
  - Extração inteligente de tabelas em PDFs
  - Normalização de dados complexos
  - Substituição de códigos por descrições
  - Geração de um arquivo .csv zipado

## Pré-requisitos Essenciais

- **Python:** 3.x
- **Java:** 8 ou maior

## Instalação

1. **Preparação do Ambiente**
```bash
git clone https://github.com/luanhmilano/intuitive-care-test.git
cd intuitive-care
python -m venv .venv
```
2. **Ativação do Ambiente Virtual**
```bash
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1

# Linux/Mac:
source .venv/bin/activate
```
3. Instalação de dependências
```bash
pip install -r requirements.txt
```

## Variáveis de ambiente
Crie um arquivo `.env` na raiz com o link da página do GOV:
```bash
TARGET_URL="https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
```

## Execução do Pipeline
### Etapa 1: Coleta de documentos (web scraping)
```bash
python run_scraping.py
```
### Saída esperada
```
data/raw/anexos_XXXXXXXXX_XXXXXX.zip
```

### Etapa 2: Transformação de dados
```bash
python run_etl.py
```
### Saída esperada
```
data/processed/Teste_luan-henrique-dos-santos-silva.zip
  └── ROL_Processado_luan-henrique-dos-santos-silva.csv
```