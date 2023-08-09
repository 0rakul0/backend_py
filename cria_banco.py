import sqlite3

conn = sqlite3.connect('banco.db')
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
     INSERT INTO hoteis VALUES ('alfa', 'Alfa Hotel', 4.3, 420.34, 'Rio de Janeiro')  
"""

cursor.execute(cria_tabela)
cursor.execute(cria_hotel)

conn.commit()
conn.close()