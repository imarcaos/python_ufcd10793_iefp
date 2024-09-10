import sqlite3
import pandas as pd

# Conectar a BD

conn = sqlite3.connect('Aula8\chinook.db')
c = conn.cursor()
c.execute("""SELECT * FROM albums;""")
resultado = c.fetchall()
conn.close()

# Apresentar dados de forma simples
# for elemento in resultado:
#     print(elemento)

# Apresentar dados usando o pandas
dados_albuns = pd.DataFrame(resultado, columns=['Id Album','Nome', 'ID do Artista'])
print(dados_albuns.head(12))

# Apresentar os dados da tabela albums
# df = pd.DataFrame(c.fetchall(), columns=['AlbumId', 'Title', 'ArtistId'])
# df.head(7)
