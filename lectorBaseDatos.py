import csv
import sys
from trie import Trie
from song import Song

sys.setrecursionlimit(10000)

archivo_csv = open('BaseDatos/spotify_data.csv', encoding='utf-8')
archivo = csv.reader(archivo_csv, delimiter = ',')

next(archivo)
trie = Trie()
for fila in archivo:
    song = Song(fila[3], fila[2], fila[1], fila[6], fila[5], fila[4], fila[18])
    trie.insert(song.getSong_name(), song)
    # print(song)
print('Fin de archivo')

trie.saveFile('BaseDatos/trieSongName.bin')    
print('Archivo creado')