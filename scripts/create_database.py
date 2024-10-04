import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('alunos_db.db')
cursor = conn.cursor()

# SQL para criar a tabela matricula_publica
create_table_sql_publica = """
CREATE TABLE IF NOT EXISTS matricula_publica (
    id INTEGER PRIMARY KEY,
    categoria TEXT NOT NULL,
    total_matriculas REAL NOT NULL,
    tipo_escola TEXT NOT NULL
);
"""

# SQL para criar a tabela matricula_privada
create_table_sql_privada = """
CREATE TABLE IF NOT EXISTS matricula_privada (
    id INTEGER PRIMARY KEY,
    categoria TEXT NOT NULL,
    total_matriculas REAL NOT NULL,
    tipo_escola TEXT NOT NULL
);
"""

# SQL para criar a tabela beneficio
create_table_sql_beneficio = """
CREATE TABLE IF NOT EXISTS beneficio (
    id INTEGER PRIMARY KEY,
    categoria TEXT NOT NULL,
    valor REAL NOT NULL
);
"""

cursor.execute(create_table_sql_publica)
cursor.execute(create_table_sql_privada)
cursor.execute(create_table_sql_beneficio)
conn.commit()

# Fechar a conexão
conn.close()

print("Tabelas criadas com sucesso!")
