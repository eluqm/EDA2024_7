import csv
from trie import Trie
from song import Song
import customtkinter as ctk
from tkinter import ttk

# Lectura del .csv
archivo_csv = open('BaseDatos/spotify_data.csv', encoding='utf-8')
archivo = csv.reader(archivo_csv, delimiter=',')
next(archivo)
trie = Trie()

count = 0  # Eliminar
for fila in archivo:
    if count >= 10000:  # Eliminar
        break  # Eliminar
    song = Song(fila[3], fila[2], fila[1], fila[6], fila[5], fila[4], fila[18])
    trie.insert(song.getSong_name(), song)
    count += 1  # Eliminar
print('Fin de archivo')

# Métodos necesarios para interactuar con la interfaz gráfica
arrSongsCoincidence = []

def getText():
    global arrSongsCoincidence
    for item in tree.get_children():
        tree.delete(item)
    songName = textbox.get("1.0", "end-1c").strip()
    author = authorbox.get("1.0", "end-1c").strip()
    year_text = yearbox.get("1.0", "end-1c").strip()
    try:
        year = int(year_text) if year_text else None
    except ValueError:
        year = None
    arrSongsCoincidence = trie.getSongAdvanced(songName if songName else None, author if author else None, year if year else None)
    for i, song in enumerate(arrSongsCoincidence):
        songValues = (i + 1, song.getSong_name(), song.getAuthor(), song.getGenre(), song.getYear(), song.getDuration())
        if i % 2 == 0:
            tree.insert("", "end", values=songValues, tags=('evenrow', song.getSong_id()))
        else:
            tree.insert("", "end", values=songValues, tags=('oddrow', song.getSong_id()))

def validateNumericInput(text):
    return text.isdigit() or text == ""

def onSelectSong(event):
    global arrSongsCoincidence
    selectedItem = tree.focus()  # El ítem seleccionado en la tabla
    if selectedItem:
        itemValuesSong = tree.item(selectedItem, 'values')  # Valores de la fila seleccionada
        app.selectedSong = arrSongsCoincidence[int(itemValuesSong[0]) - 1]
        print(f"Canción seleccionada: {app.selectedSong}")  # Objeto Song
        print(app.selectedSong.getSong_id())  # song_id

def onDoubleClickSong(event):
    global arrSongsCoincidence
    selectedItem = tree.focus()
    if selectedItem:
        itemValuesSong = tree.item(selectedItem, 'values')
        app.selectedSong = arrSongsCoincidence[int(itemValuesSong[0]) - 1]
        print(f"Doble clic en la canción: {app.selectedSong}")
        print(app.selectedSong.getSong_id())

def buttonClick():
    if hasattr(app, 'selectedSong') and app.selectedSong:
        print(f"Retornando el objeto Song: {app.selectedSong}")
        return app.selectedSong
    else:
        print("No se ha seleccionado ninguna canción.")

# Configuración de la interfaz gráfica
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("dark-blue")  

app = ctk.CTk()
app.geometry("700x500")
app.configure(bg="#121212")  

main = ctk.CTkFrame(app, fg_color="#1e1e1e")  
main.pack(fill="both", expand=True, padx=10, pady=10)

input_frame = ctk.CTkFrame(main, fg_color="#1e1e1e")
input_frame.pack(pady=10)

ctk.CTkLabel(input_frame, text="Nombre de canción:", text_color="#ffffff").grid(row=0, column=0, padx=5, pady=5)
textbox = ctk.CTkTextbox(input_frame, width=150, height=30, fg_color="#2e2e2e", text_color="#ffffff")
textbox.grid(row=0, column=1, padx=5, pady=5)

ctk.CTkLabel(input_frame, text="Autor:", text_color="#ffffff").grid(row=0, column=2, padx=5, pady=5)
authorbox = ctk.CTkTextbox(input_frame, width=150, height=30, fg_color="#2e2e2e", text_color="#ffffff")
authorbox.grid(row=0, column=3, padx=5, pady=5)

ctk.CTkLabel(input_frame, text="Año:", text_color="#ffffff").grid(row=0, column=4, padx=5, pady=5)
yearbox = ctk.CTkTextbox(input_frame, width=50, height=30, fg_color="#2e2e2e", text_color="#ffffff")
yearbox.grid(row=0, column=5, padx=5, pady=5)

button = ctk.CTkButton(main, text="Buscar", command=getText, fg_color="#5a5a5a", hover_color="#3a3a3a", text_color="#ffffff")
button.pack(pady=10)

table = ctk.CTkFrame(main, fg_color="#1e1e1e")
table.pack(pady=10, fill="both", expand=True)
columns = ("Coincidencia", "Nombre", "Autor", "Género", "Año", "Duración")
tree = ttk.Treeview(table, columns=columns, show="headings", height=30)
for col in columns:
    tree.heading(col, text=col, anchor="center")
    tree.column(col, width=100, anchor="center")
scroll_y = ttk.Scrollbar(table, orient="vertical", command=tree.yview)
scroll_y.pack(side="right", fill="y")
tree.configure(yscroll=scroll_y.set)
tree.pack(fill="x", expand=False)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
                background="#2e2e2e",
                foreground="#ffffff",
                fieldbackground="#2e2e2e",
                rowheight=25)
style.configure("Treeview.Heading",
                background="#3a3a3a",
                foreground="#ffffff",
                font=("Arial", 10, "bold"))
style.map("Treeview",
          background=[("selected", "#5a5a5a")],
          foreground=[("selected", "#ffffff")])
style.map("Treeview.Heading",
          background=[("active", "#3a3a3a")])

tree.tag_configure('oddrow', background='#3a3a3a')
tree.tag_configure('evenrow', background='#2e2e2e')

tree.bind('<<TreeviewSelect>>', onSelectSong)
tree.bind('<Double-1>', onDoubleClickSong)

app.mainloop()