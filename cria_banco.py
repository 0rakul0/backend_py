import sqlite3

conn = sqlite3.connect('./instance/banco.db')
cursor = conn.cursor()

cria_tabela = """
    CREATE TABLE IF NOT EXISTS hoteis (
        hotel_id text Primary KEY,
        nome text, 
        estrelas real,
        diaria real, 
        cidade text
    )
"""

cria_hotel = """
     INSERT INTO hoteis VALUES ('beta', 'Beta Hotel', 4.0, 300.00, 'São Paulo')  
"""

cursor.execute(cria_tabela)
cursor.execute(cria_hotel)

conn.commit()
conn.close()