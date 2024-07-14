import csv

from trie import Trie
from song import Song

archivo_csv = open('BaseDatos/spotify_data.csv', encoding='utf-8')
archivo = csv.reader(archivo_csv, delimiter = ',')

next(archivo)
trie = Trie()
for fila in archivo:
    song = Song(fila[3], fila[2], fila[1], fila[6], fila[5], fila[4], fila[18])
    print(song)
    # print(fila[0])
print('Fin de archivo')