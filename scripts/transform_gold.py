import pandas as pd 
import sqlite3


# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('alunos_db.db')
cursor = conn.cursor()

#load dados escolas publicas

df_escolas_publicas = pd.read_csv('data/silver/matriculas_sp_escolas.csv')
df_escolas_publicas.rename(columns={'Tipo de Escola':'tipo_escola'}, inplace=True)
df_escolas_publicas = df_escolas_publicas[df_escolas_publicas['tipo_escola'] == 'Pública']

df_escolas_publicas.to_sql('matricula_publica', conn, if_exists='append', index=False)

#load dados escolas privadas

df_escolas_privadas = pd.read_csv('data/silver/matriculas_sp_escolas.csv')
df_escolas_privadas.rename(columns={'Tipo de Escola':'tipo_escola'}, inplace=True)
df_escolas_privadas = df_escolas_privadas[df_escolas_privadas['tipo_escola'] == 'Privada']
df_escolas_privadas.to_sql('matricula_privada', conn, if_exists='append', index=False)



#load dados beneficios
df_beneficios = pd.read_csv('data/silver/auxilio_materiais.csv')
df_beneficios.to_sql('beneficio', conn, if_exists='replace', index=False)




cursor.close()
conn.commit()