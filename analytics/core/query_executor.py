import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
db_conn = os.getenv('DB_CONN')

class QueryExecutor:
    def __init__(self):
        self.engine = create_engine(db_conn)
    
    def get_top_operadoras(self, period: str) -> pd.DataFrame:
        """
        period: 'last_quarter' ou 'last_year'
        Retorna DataFrame com as 10 maiores operadoras
        """
        with self.engine.connect() as conn:
            if period == 'last_quarter':
                query = text("""
                    SELECT o.nome_fantasia, SUM(d.vl_saldo_final) AS total
                    FROM demonstracoes_contabeis d
                    JOIN operadoras o ON d.reg_ans = o.registro_ans
                    WHERE MATCH(d.descricao) AGAINST(
                        'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
                        IN NATURAL LANGUAGE MODE
                    )
                    AND d.periodo = (
                        SELECT MAX(periodo) FROM demonstracoes_contabeis
                    )
                    GROUP BY o.nome_fantasia
                    ORDER BY total DESC
                    LIMIT 10
                """)
            else:
                query = text("""
                    SELECT o.nome_fantasia, SUM(d.vl_saldo_final) AS total
                    FROM demonstracoes_contabeis d
                    JOIN operadoras o ON d.reg_ans = o.registro_ans
                    WHERE MATCH(d.descricao) AGAINST(
                        'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
                        IN NATURAL LANGUAGE MODE
                    )
                    AND d.data >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
                    GROUP BY o.nome_fantasia
                    ORDER BY total DESC
                    LIMIT 10
                """)

        result = conn.execute(query)
        return pd.DataFrame(result.fetchall(), columns=result.keys())