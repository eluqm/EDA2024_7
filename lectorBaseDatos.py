import csv
import sys
from trie import Trie
from song import Song
import customtkinter as ctk
from tkinter import ttk
import tkinter as tk



archivo_csv = open('BaseDatos/spotify_data.csv', encoding='utf-8')
archivo = csv.reader(archivo_csv, delimiter = ',')

next(archivo)
trie = Trie()
for fila in archivo:
    song = Song(fila[3], fila[2], fila[1], fila[6], fila[5], fila[4], fila[18])
    trie.insert(song.getSong_name(), song)
    # print(song)
print('Fin de archivo')
"""
cancion = Song("53QF56cjZA9RTuuMZDrSA6","Hello","Jason Mraz", "acoustic", 2012, 68, 240166)
print(cancion)
cancion1 = Song("53QF56cjZA9RTuuMZDrS44","Hello","Michael Jackson", "pop", 2012, 68, 3725000)
print(cancion1)
cancion2 = Song("ghtF56cjZA9RTuuMZDrSA6","Its my live","Bon Jovi", "rock", 2002, 68, 2725000)
print(cancion2)

trie = Trie()
trie.insert(cancion.getSong_name(), cancion)
trie.insert(cancion1.getSong_name(), cancion1)
trie.insert(cancion2.getSong_name(), cancion2)
"""

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x440")

def getText():
    for item in tree.get_children():
        tree.delete(item)

    songName = textbox.get("1.0", "end-1c")
    
    arrSongs = trie.getSong(songName)
    for song in arrSongs:
        tree.insert("", "end", values=(song.getSong_name(), song.getAuthor(), song.getGenre(), song.getYear(), song.getDuration()))

main = ctk.CTkFrame(app)
main.pack(fill="both", expand=True, padx=10, pady=10)

ctk.CTkLabel(main, text="Nombre de cancion").pack(pady=10)
    
textbox = ctk.CTkTextbox(main, width=200, height=50)
textbox.pack(pady=10)

button = ctk.CTkButton(main, text="Buscar", command=getText)
button.pack(pady=10)

table = ctk.CTkFrame(main)
table.pack(pady=10, fill="both", expand=True)
columns = ("Nombre", "Autor", "Género", "Año", "Duración")
tree = ttk.Treeview(table, columns=columns, show="headings", height=8)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=80, anchor="center")
scroll_y = ttk.Scrollbar(table, orient="vertical", command=tree.yview)
scroll_y.pack(side="right", fill="y")
tree.configure(yscroll=scroll_y.set)
tree.pack(fill="x", expand=False)

app.mainloop()