import sqlite3 as lite

#criar conexao com banco
con = lite.connect('db.sistema-academico.db')

#criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS CADASTRO_ALUNO (MATRICULA INTEGER PRIMARY KEY, NOME TEXT, SERIE INTEGER, " \
                "TURNO TEXT, TURMA INTEGER)")