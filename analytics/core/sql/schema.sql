CREATE DATABASE IF NOT EXISTS `intuitive_care-db`;
USE `intuitive_care-db`;

CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans VARCHAR(6) NOT NULL,
    cd_conta_contaabil VARCHAR(15) NOT NULL,
    descricao TEXT NOT NULL,
    vl_saldo_inicial DECIMAL(15, 2),
    vl_saldo_final DECIMAL(15, 2),
    periodo CHAR(6),
    INDEX idx_periodo (periodo),
    INDEX idx_conta (cd_conta_contabil),
    FULLTEXT idx_descricao (descricao)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;;

CREATE TABLE IF NOT EXISTS operadoras (
    registro_ans VARCHAR(6) PRIMARY KEY,
    cnpj VARCHAR(14) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(50),
    logradouro VARCHAR(255),
    numero VARCHAR(50),
    complemento VARCHAR(255),
    bairro VARCHAR(50),
    cidade VARCHAR(255),
    uf VARCHAR(2),
    cep VARCHAR(8),
    ddd VARCHAR(2),
    telefone VARCHAR(50),
    fax VARCHAR(50),
    endereco_eletronico VARCHAR(50),
    representante VARCHAR(255),
    cargo_representante VARCHAR(50),
    regiao_de_comercializacao VARCHAR(50),
    data_registro_ans DATE NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
