import csv

archivo_csv = open('BaseDatos/spotify_data.csv', encoding='utf-8')
archivo = csv.reader(archivo_csv, delimiter = ',')

next(archivo)

for fila in archivo:
    if (int(fila[18])) > 3599000:
        print(fila[18])
print('Fin de archivo')