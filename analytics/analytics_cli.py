import click
from tabulate import tabulate
from core.data_loader import load_data
from core.query_executor import QueryExecutor

@click.group()
def cli():
    """CLI para Análise de Dados de Saúde"""
    pass

@cli.command()
def load():
    """Carrega dados no MySQL"""
    try:
        load_data()
        click.echo("Dados carregados com sucesso!")
    except Exception as e:
        click.echo(f"Erro no carregamento: {str(e)}")

@cli.command()
@click.option('--period', 
             type=click.Choice(['quarter', 'year'], case_sensitive=False),
             required=True,
             help="Período para análise: 'quarter' ou 'year'")
def analyze(period):
    """Executa análise dos dados"""
    executor = QueryExecutor()
    
    result = executor.get_top_operadoras(
        'last_quarter' if period == 'quarter' else 'last_year'
    )
    
    click.echo("\n🔍 Resultado da Análise:")
    print(tabulate(result, headers='keys', tablefmt='psql', showindex=False))

if __name__ == '__main__':
    cli()