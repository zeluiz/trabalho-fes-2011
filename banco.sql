BEGIN;
CREATE TABLE "registros_categoria" (
    "id" integer NOT NULL PRIMARY KEY,
    "nome_categoria" varchar(20) NOT NULL,
    "descricao_categoria" varchar(200) NOT NULL
)
;
CREATE TABLE "registros_receita" (
    "id" integer NOT NULL PRIMARY KEY,
    "nome_receita" varchar(40) NOT NULL,
    "descricao_receita" varchar(200) NOT NULL,
    "categoria_id" integer NOT NULL REFERENCES "registros_categoria" ("id"),
    "valor_receita" real NOT NULL,
    "data_receita" datetime NOT NULL
)
;
CREATE TABLE "registros_despesa" (
    "id" integer NOT NULL PRIMARY KEY,
    "nome_despesa" varchar(40) NOT NULL,
    "descricao_despesa" varchar(200) NOT NULL,
    "categoria_id" integer NOT NULL REFERENCES "registros_categoria" ("id"),
    "valor_despesa" real NOT NULL,
    "data_despesa" datetime NOT NULL
)
;
CREATE TABLE "login_usuario" (
    "id" integer NOT NULL PRIMARY KEY,
    "nome" varchar(15) NOT NULL,
    "senha" varchar(12) NOT NULL,
    "email" varchar(75) NOT NULL,
    "tipo" varchar(13) NOT NULL,
    "dataEntrada" datetime NOT NULL
)
;
COMMIT;
