DROP DATABASE IF EXISTS scuola;
CREATE DATABASE scuola;
USE scuola;

CREATE TABLE province(
    sigla CHAR(2) PRIMARY KEY,
    nome VARCHAR(25) 
);
CREATE TABLE classi(
    id INT PRIMARY KEY,
    classe CHAR(1) UNIQUE,
    sezione CHAR(1) UNIQUE,
    indirizzo CHAR(1) UNIQUE,
    anno_scolastico CHAR(4) UNIQUE
);

CREATE TABLE studenti(
    cf CHAR(16) PRIMARY KEY, --Codice Fiscale
    cognome VARCHAR(25),
    nome VARCHAR(25),
    classe CHAR(3),
    provincia CHAR(2),
    FOREIGN KEY(classe) REFERENCES classi(classe, sezione, indirizzo),
    FOREIGN KEY(provincia) REFERENCES province(sigla)
);
