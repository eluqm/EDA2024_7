import csv
import sys
from trie import Trie
from song import Song
import customtkinter as ctk
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

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x240")

def getText():
    text = textbox.get("1.0", "end-1c")
    print(trie.getSong(text))
    
ctk.CTkLabel(app, text="Nombre de cancion").pack()
    
textbox = ctk.CTkTextbox(app, width=200, height=50)
textbox.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

button = ctk.CTkButton(master=app, text="Buscar", command=getText)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

app.mainloop()