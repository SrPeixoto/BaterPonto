import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
import re
import time

# ===============>> CONEXÃO <<===============

config = {
  'user': 'u526069146_resoluteIT',
  'password': '3f:1wsIL^c',
  'host': 'sql532.main-hosting.eu',
  'database': 'u526069146_pResoluteIT',
  'raise_on_warnings': True
}



def criar_con():
    conn = None
    try:
        conn = mysql.connector.connect(**config)
        print("\nDataBase Conectada!")
        return conn
    except mysql.connector.Error as err:
        print(err)

    return conn

def C_Tabelas(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except mysql.connector.Error as err:
        print(err)



def mainC_Tabelas():

    sql_1 = """CREATE TABLE IF NOT EXISTS Entrada (
                                    id integer PRIMARY KEY AUTO_INCREMENT,
                                    Nome text NOT NULL,
                                    N_Crachá text NOT NULL,
                                    CPF text,
                                    Data text,
                                    Hora text,
                                    Atendente text
                                );"""

    sql_2 = """CREATE TABLE IF NOT EXISTS Admins (
                                    id integer PRIMARY KEY AUTO_INCREMENT,
                                    Usuario text NOT NULL,
                                    Senha text NOT NULL,
                                    N_Crachá text,
                                    Nome text
                                );"""

    sql_3 = """CREATE TABLE IF NOT EXISTS Funcionarios (
                                    id integer PRIMARY KEY AUTO_INCREMENT,
                                    Nome text NOT NULL,
                                    N_Crachá text NOT NULL,
                                    CPF text NOT NULL,
                                    Email text NOT NULL,
                                    Fone text NOT NULL,
                                    Cidade text NOT NULL,
                                    Atendente text NOT NULL
                                );"""


    conn = criar_con()
    if conn is not None:
        C_Tabelas(conn, sql_1)
        C_Tabelas(conn, sql_2)
        C_Tabelas(conn, sql_3)
    else:
        print("Erro! A conexão com o banco de dados não foi estabelecida.")

if __name__ == '__main__':
    mainC_Tabelas()


