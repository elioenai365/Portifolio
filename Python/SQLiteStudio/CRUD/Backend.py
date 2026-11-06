#Nesta etapa, vamos resolver um dos requisitos de nossa aplicação.
# Ela deverá realizar um CRUD, ou seja: ler, escrever, atualizar e
# apagar (Create, Read, Update e Delete). Para isso, devemos ter um
# banco de dados e uma tabela (clientes) com os seguintes campos:
#ID
#Nome
#Sobrenome
#E-mail
#CPF

import sqlite3 as sql

class TransactionObject():
    """Classe responsável por gerenciar a conexão, cursor e transações com o SQLite."""
    database = "clientes.db"
    connection = None
    cursor = None
    connected = False

    def connect(self):# realiza a conexão com o banco de dados
        TransactionObject.connection = sql.connect(TransactionObject.database)
        TransactionObject.cursor = TransactionObject.connection.cursor()
        TransactionObject.connected = True

    def disconnect(self):# Encerra a conexao com BD
        TransactionObject.connection.close()
        TransactionObject.connected = False

    def execute(self, sql, parms = None):#Executa um comando no BD pelos parâmentros
    # Self: Referência ao propio objeto, Sql: Comando que dever ser executado
    #parms:Vetor que contém os parâmentros do comando SQL e pode ser omitdo

        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cursor.execute(sql)
            else:
                TransactionObject.cursor.execute(sql, parms)
            return True
        else:
            return False

#obtém os valores de entrada do comando SELECT
    def fetchall(self):
        return TransactionObject.cursor.fetchall()

#FAz o commit das operações
    def persist(self):
        if TransactionObject.connected:
            TransactionObject.connection.commit()
            return True
        else:
            return False

def initDB():
    trans= TransactionObject()
    trans.connect()

    trans.execute("Create table if not exists clientes(id integer primary key, nome text, sobrenome text, email text, cpf text)")
    trans.persist()
    trans.disconnect()

def insert (nome, sobrenome, email, cpf):
    trans= TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO clientes VALUES(NULL, ?, ?,?,?)", (nome, sobrenome, email, cpf))
    trans.persist()
    trans.disconnect()

def view():
    trans= TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM clientes")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def search(nome = "", sobrenome = "", email = "", cpf = ""):
    trans= TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM clientes WHERE nome = ? or sobrenome = ? or email=? or cpf=?",
                  (nome,sobrenome,email,cpf))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def delete(id):
    trans= TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM clientes WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()

def update(id, nome, sobrenome, email, cpf):
    trans= TransactionObject()
    trans.connect()

    trans.execute("UPDATE clientes SET nome =? , sobrenome=? , email=?, cpf=? WHERE id = ?",
                  (nome, sobrenome, email, cpf, id))

    trans.persist()
    trans.disconnect()

initDB()

print("tudo certo")