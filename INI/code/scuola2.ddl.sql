DROP DATABASE IF EXISTS scuola;
CREATE DATABASE scuola;
USE scuola;

CREATE TABLE province(
    sigla CHAR(2) PRIMARY KEY,
    nome VARCHAR(25)
);
CREATE TABLE classi(
    nome CHAR(8) PRIMARY KEY,
    anno_scolastico CHAR(8)
);

CREATE TABLE studenti(
    cf CHAR(16) PRIMARY KEY, --Codice Fiscale
    cognome VARCHAR(25) NOT NULL,
    nome VARCHAR(25) NOT NULL,
    classe CHAR(8),
    provincia CHAR(2) DEFAULT "VR",
    FOREIGN KEY(classe) REFERENCES classi(nome),
    FOREIGN KEY(provincia) REFERENCES province(sigla)
);
