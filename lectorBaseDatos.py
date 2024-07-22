import csv
import sys
from trie import Trie
from song import Song
import customtkinter as ctk
from tkinter import ttk
import tkinter as tk

# Lectura del .csv
archivo_csv = open('BaseDatos/spotify_data.csv', encoding='utf-8')
archivo = csv.reader(archivo_csv, delimiter = ',')
next(archivo)
trie = Trie()
for fila in archivo:
    song = Song(fila[3], fila[2], fila[1], fila[6], fila[5], fila[4], fila[18])
    trie.insert(song.getSong_name(), song)
print('Fin de archivo')

# Metodos necesarios para interactuar con la interfaz grafica
arrSongsCoincidence = []
def getText():
    global arrSongsCoincidence
    for item in tree.get_children():
        tree.delete(item)

    songName = textbox.get("1.0", "end-1c")
    
    arrSongsCoincidence = trie.getSong(songName)
    for i, song in enumerate(arrSongsCoincidence):
        songValues = (i+1 ,song.getSong_name(), song.getAuthor(), song.getGenre(), song.getYear(), song.getDuration())
        tree.insert("", "end", values=songValues, tags=(song.getSong_id(),))

def onSelectSong(event):
    global arrSongsCoincidence
    selectedItem = tree.focus()  #  El ítem seleccionado en la tabla
    if selectedItem:
        itemValuesSong = tree.item(selectedItem, 'values')  # Valores de la fila seleccionada
        app.selectedSong = arrSongsCoincidence[int(itemValuesSong[0]) - 1]
        print(f"Canción seleccionada: {app.selectedSong}") #Objeto Song
        print(app.selectedSong.getSong_id()) # song_id
        
def onDoubleClickSong(event):
    global arrSongsCoincidence
    selectedItem = tree.focus()
    if selectedItem:
        itemValuesSong = tree.item(selectedItem, 'values')
        app.selectedSong = arrSongsCoincidence[int(itemValuesSong[0])]
        print(f"Doble clic en la canción: {app.selectedSong}")
        print(app.selectedSong.getSong_id())
        
def buttonClick():
    if hasattr(app, 'selectedSong') and app.selectedSong:
        print(f"Retornando el objeto Song: {app.selectedSong}")
        return app.selectedSong
    else:
        print("No se ha seleccionado ninguna canción.")

# Elementos de la interfaz grafica
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x500")

main = ctk.CTkFrame(app)
main.pack(fill="both", expand=True, padx=10, pady=10)

ctk.CTkLabel(main, text="Nombre de cancion").pack(pady=10)
    
textbox = ctk.CTkTextbox(main, width=200, height=50)
textbox.pack(pady=10)

ctk.CTkLabel(main, text="Año de la canción").pack(pady=10)

#validate_numeric_cmd = app.register(validate_numeric_input)
#yearbox = ctk.CTkTextbox(main, width=200, height=50)
#yearbox.pack(pady=10)
#yearbox.configure(validate="key", validatecommand=(validate_numeric_cmd, "%P"))

button = ctk.CTkButton(main, text="Buscar", command=getText)
button.pack(pady=10)

table = ctk.CTkFrame(main)
table.pack(pady=10, fill="both", expand=True)
columns = ("Coincidencia","Nombre", "Autor", "Género", "Año", "Duración")
tree = ttk.Treeview(table, columns=columns, show="headings", height=30)# height=8
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=80, anchor="center")
scroll_y = ttk.Scrollbar(table, orient="vertical", command=tree.yview)
scroll_y.pack(side="right", fill="y")
tree.configure(yscroll=scroll_y.set)
tree.pack(fill="x", expand=False)

# Eventos para las canciones
tree.bind('<<TreeviewSelect>>', onSelectSong)
tree.bind('<Double-1>', onDoubleClickSong)

app.mainloop()