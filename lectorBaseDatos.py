import csv

archivo_csv = open('BaseDatos/spotify_data.csv')
archivo = csv.reader(archivo_csv, delimiter = ',')

for fila in archivo:
    print(fila)
print('Fin de archivo')