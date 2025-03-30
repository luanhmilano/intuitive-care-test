COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/data/raw/demonstracoes_contabeis-{ano}/{arquivo}.csv'
DELIMITER ';' CSV HEADER ENCODING 'LATIN1';

COPY operadoras FROM '/data/raw/operadoras_ativas/Relatorio_cadop.csv'
DELIMITER ';' CSV HEADER ENCODING 'LATIN1';