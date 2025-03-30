-- Query 1: Top 10 último trimestre
WITH ultimo_trimestre AS (
    SELECT MAX(periodo) AS periodo 
    FROM demonstracoes_contabeis
)
SELECT 
    o.nome_fantasia,
    SUM(d.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.reg_ans = o.registro_ans
WHERE d.descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND d.periodo = (SELECT periodo FROM ultimo_trimestre)
GROUP BY o.nome_fantasia
ORDER BY total_despesas DESC
LIMIT 10;

-- Query 2: Top 12 meses
SELECT 
    o.nome_fantasia,
    SUM(d.vl_saldo_final) AS total_despesas,
    COUNT(DISTINCT d.periodo) AS trimestres_considerados
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.reg_ans = o.registro_ans
WHERE d.descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND d.data >= CURRENT_DATE - INTERVAL '1 YEAR'
GROUP BY o.nome_fantasia
ORDER BY total_despesas DESC
LIMIT 10;