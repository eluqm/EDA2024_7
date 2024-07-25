import csv
import test_grafos
from customtkinter import *
from tkinter import *
from tkinter import ttk
from PIL import Image
from song import Song
from linkedList import LinkedList
from b_plus_tree import BPlusTree
from trie import Trie

# 
general_song = None 
song_item_frames = []
#my_song_list = LinkedList()

# List general
general_Playlist = LinkedList()

# Conjunto de playlist
original_PlayList = LinkedList()
random_PlayList = LinkedList()
song_id_PlayList = LinkedList()
song_name_PlayList = LinkedList()
author_PlayList = LinkedList()
genre_PlayList = LinkedList()
year_PlayList = LinkedList()
popularity_PlayList = LinkedList()
duration_PlayList = LinkedList()

# Conjunto de arboles b+
song_id_bplustree = BPlusTree()
song_name_bplustree = BPlusTree()
author_bplustree = BPlusTree()
genre_bplustree = BPlusTree()
year_bplustree = BPlusTree()
popularity_bplustree = BPlusTree()
duration_bplustree = BPlusTree()

# Actualizar lista
def update_general_list():
    global song_item_frames
    global general_Playlist
    if (len(song_item_frames) > 0):
        for songItem in song_item_frames:
            songItem.song_interface.song_item.pack_forget()
    song_item_frames.clear()
    current = general_Playlist.head
    for _ in range(general_Playlist.size):
        song_item_frames.append(SongItem(scrollist, current.song, len(song_item_frames)))
        current = current.next
    print(len(song_item_frames))

def update_list(list):
    for songItem in song_item_frames:
            songItem.song_interface.song_item.pack_forget()
    song_item_frames.clear()
    for song_item in list:
        general_Playlist.add_song(song_item)
        song_item_frames.append(SongItem(scrollist, song_item, len(song_item_frames)))



# Agregar cancion
def add_new_song():
    if general_song is not None:
        add_song(general_song)


def add_song(song):
    global general_Playlist
    original_PlayList.add_song(song)
    original_PlayList.print()
    song_id_bplustree.insert(getattr(song, 'song_id'), song)
    song_name_bplustree.insert(getattr(song, 'song_name'), song)
    author_bplustree.insert(getattr(song, 'author'), song)
    genre_bplustree.insert(getattr(song, 'genre'), song)
    year_bplustree.insert(getattr(song, 'year'), song)
    popularity_bplustree.insert(getattr(song, 'popularity'), song)
    duration_bplustree.insert(getattr(song, 'duration'), song)
    general_Playlist = original_PlayList
    update_general_list()

def view_graph():
    test_grafos.main()


window = CTk()
window.title("Music Player")
window.geometry("1560x500")#860
window.configure(fg_color='black')
set_appearance_mode("darck")

default_icon_data = Image.open("src/default-icon.jpeg")
default_icon = CTkImage(dark_image=default_icon_data, light_image=default_icon_data, size=(200, 200))
home_icon_data = Image.open("src/home-icon.png")
home_icon = CTkImage(dark_image=home_icon_data, light_image=home_icon_data, size=(40, 40))
loupe_icon_data = Image.open("src/loupe-icon.png")
loupe_icon = CTkImage(dark_image=loupe_icon_data, light_image=loupe_icon_data, size=(40, 40))
graf_icon_data = Image.open("src/graf-icon.png")
graf_icon = CTkImage(dark_image=graf_icon_data, light_image=graf_icon_data, size=(40, 40))

# Menu lateral
menu = CTkFrame(master=window, width=75, height=500, fg_color="#272727", corner_radius=0)
menu.pack(expand=True, side="left")

button_home = CTkButton(master=menu, text="", width=40, height=40, fg_color="#272727", image=home_icon, command=lambda: print("Ventana Principal"))
button_home.place(relx=0.5, rely=0.1, anchor="center")
button_search = CTkButton(master=menu, text="", width=40, height=40, fg_color="#272727", image=loupe_icon, command=lambda: print("Ventana Buscar"))
button_search.place(relx=0.5, rely=0.24, anchor="center")
button_graf = CTkButton(master=menu, text="", width=40, height=40, fg_color="#272727", image=graf_icon, command=view_graph)
button_graf.place(relx=0.5, rely=0.37, anchor="center")

# Reproductor
player = CTkFrame(master=window, width=375, height=500, fg_color="#000000", corner_radius=0)
player.pack(expand=True, side="left")
CTkLabel(master=player, text="", image=default_icon).place(relx=0.5, rely=0.3, anchor="center")
CTkLabel(master=player, text="Nombre canción", text_color="#ffffff", font=("Arial Bold", 24)).place(relx=0.5, rely=0.6, anchor="center")
CTkLabel(master=player, text="Artista", text_color="#ffffff", font=("Arial Bold", 16)).place(relx=0.5, rely=0.7, anchor="center")
slider = CTkSlider(master=player, from_=0, to=100, number_of_steps=5, button_color="#C850C0", progress_color="#C850C0").place(relx=0.5, rely=0.8, anchor="center")

# Lista de reproduccion
playlist = CTkFrame(master=window, width=390, height=450, fg_color="#272727", corner_radius=0,)
playlist.pack(expand=True, side="left", pady=(30, 20), padx=(0, 20))
optionsPlayList = CTkFrame(master=playlist, width=390, height=40, fg_color="#1a1a1a", corner_radius=0,)
optionsPlayList.pack(expand=True, side="top")
namePlayList = CTkLabel(master=optionsPlayList, text="My Play List", text_color="#ffffff", font=("Arial Bold", 20), width=110, height=40, anchor="w", corner_radius=0)
namePlayList.pack(side="left",  padx=(10, 110))
textOrder = CTkLabel(master=optionsPlayList, text="Orden:", text_color="#ffffff", font=("Times new Roman", 15), width=50, height=20, anchor="e", corner_radius=0)
textOrder.pack(side="left",  padx=(0, 5))

# Menu desplegable
def opcion_seleccionada(opcion):
    global general_Playlist
    match opcion:
        case "Original":
            general_Playlist = original_PlayList
            update_general_list()
        case "Random":
            general_Playlist = original_PlayList.random_play()
            update_general_list()
        case "ID ↑":
            general_Playlist = song_id_PlayList
            update_list(song_id_bplustree.traverse_all_values())
        case "ID ↓":
            general_Playlist = song_id_PlayList
            update_list(reversed(song_id_bplustree.traverse_all_values()))
        case "Nombre ↑":
            general_Playlist = song_name_PlayList
            update_list(song_name_bplustree.traverse_all_values())
        case "Nombre ↓":
            general_Playlist = song_name_PlayList
            update_list(reversed(song_name_bplustree.traverse_all_values()))
        case "Autor ↑":
            general_Playlist = author_PlayList
            update_list(author_bplustree.traverse_all_values())
        case "Autor ↓":
            general_Playlist = author_PlayList
            update_list(reversed(author_bplustree.traverse_all_values()))
        case "Genero ↑":
            general_Playlist = genre_PlayList
            update_list(genre_bplustree.traverse_all_values())
        case "Genero ↓":
            general_Playlist = genre_PlayList
            update_list(reversed(genre_bplustree.traverse_all_values()))
        case "Año ↑":
            general_Playlist = year_PlayList
            update_list(year_bplustree.traverse_all_values())
        case "Año ↓":
            general_Playlist = year_PlayList
            update_list(reversed(year_bplustree.traverse_all_values()))
        case "Popular ↑":
            general_Playlist = popularity_PlayList
            update_list(popularity_bplustree.traverse_all_values())
        case "Popular ↓":
            general_Playlist = popularity_PlayList
            update_list(reversed(popularity_bplustree.traverse_all_values()))
        case "Duración ↑":
            general_Playlist = duration_PlayList
            update_list(duration_bplustree.traverse_all_values())
        case "Duración ↓":
            general_Playlist = duration_PlayList
            update_list(reversed(duration_bplustree.traverse_all_values()))
        case _:
            return "Invalid option"
        

optionsOrder = ["Original", "Random", "ID ↑", "ID ↓", "Nombre ↑", "Nombre ↓", "Autor ↑", "Autor ↓", "Genero ↑", "Genero ↓", "Año ↑", "Año ↓", "Popular ↑", "Popular ↓", "Duración ↑", "Duración ↓"]
drop_down_menu = CTkOptionMenu(master=optionsPlayList, values=optionsOrder, command=opcion_seleccionada, width=100, height=20)
drop_down_menu.pack(side="left", padx=(0, 5))


scrollist = CTkScrollableFrame(master=playlist, width=390, height=400, fg_color="#272727", corner_radius=0,)
scrollist.pack(expand=True, side="top")



class SongItem_Interface:
    def __init__(self, list, song):

        # Elemento cancion
        self.song_item = CTkFrame(master=list, width=380, height=50, fg_color="#000000", corner_radius=0)
        self.song_item.pack(pady=0.5)

        # Imagen
        self.icon_song_data = Image.open("src/default-icon.jpeg")
        self.icon_song = CTkImage(dark_image=self.icon_song_data, light_image=self.icon_song_data, size=(40, 40))
        self.label_icon_song = CTkLabel(master=self.song_item, text="", image=self.icon_song, width=50, height=50)
        self.label_icon_song.pack(side="left")
        # Datos de la cancion
        self.specifications = CTkFrame(master=self.song_item, width=210, height=50, fg_color="#000000", corner_radius=0)
        self.specifications.pack(side="left", padx=(0, 0))
        self.song_name = CTkLabel(master=self.specifications, text=song.getSong_name(), text_color="#ffffff", font=("Arial Bold", 15), width=210, height=30, anchor="w")
        self.song_name.pack(pady=(0, 0))
        self.song_data = CTkLabel(master=self.specifications, text=song.getAuthor(), text_color="#ffffff", font=("Arial Bold", 10), width=210, height=20, anchor="w")
        self.song_data.pack(pady=(0, 0))
        # Duracion
        self.duration = CTkLabel(master=self.song_item, text=song.getDuration(), text_color="#ffffff", font=("Arial Bold", 10), width=60, height=20, anchor="e", corner_radius=0)
        self.duration.pack(side="left", pady=(30, 0), padx=(0, 0))
        # Boton de movimiento
        self.position = CTkFrame(master=self.song_item, width=60, height=50, fg_color="#000000", corner_radius=0)
        self.position.pack(side="left", padx=(0, 0))
        self.icon_position_data = Image.open("src/position-icon.png")
        self.icon_position = CTkImage(dark_image=self.icon_position_data, light_image=self.icon_position_data, size=(30, 10))
        self.button_position = CTkButton(master=self.position, text="", width=30, height=16, fg_color="#000000", image=self.icon_position)
        self.button_position.place(relx=0.5, rely=0.5, anchor="center")
        #self.button_position = CTkButton(master=self.position, text="D", command=delete, width=10, height=16, fg_color="#000000")
        #self.button_position.place(relx=0.9, rely=0.9, anchor="center")

class SongItem:
    def __init__(self, list, song, index):
        self.index = index
        self.indexControl = index
        self.song_interface = SongItem_Interface(list, song)
        self.song_interface.button_position.bind('<Button-1>', self.save_mouse_position)
        self.song_interface.button_position.bind('<B1-Motion>', self.on_drag)
        self.song_interface.button_position.bind('<ButtonRelease-1>', self.on_button_release)
        self.drag_data = {"x": 0, "y": 0, "item": None}
    
    def __str__(self):
        return f"{self.index}, {self.song_interface.song}"
    
    def save_mouse_position(self, event):
        print("click")
        self.drag_data["item"] = self.index
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_drag(self, event):
        print("mover")
        if self.drag_data["item"] is None:
            return

        item_index = self.drag_data["item"]
        new_index = self.nearest_songItem(event.y_root)

        if new_index != item_index and new_index is not None:
            self.move_item(item_index, new_index)
            self.drag_data["item"] = new_index
    
    def on_button_release(self, event):
        print("final")
        if self.drag_data["item"] is None:
            return
        
        #item_index = self.drag_data["item"]
        new_index = self.nearest_songItem(event.y_root)

        print(f"item_index: {self.indexControl}, new_index: {new_index}")

        if new_index != self.indexControl and new_index is not None:
            print(f"Cambiando orden de {self.indexControl} a {new_index}")
            general_Playlist.change_order(self.indexControl, new_index)
            SongItem.update_indexControl()
    
    def move_item(self, from_index, to_index):
        if from_index == to_index:
            return

        item = song_item_frames.pop(from_index)
        song_item_frames.insert(to_index, item)

        SongItem.reposition_songItems()

    def nearest_songItem(self, y):
        index_songItem = None
        min_distance = float('inf')

        for songItem in song_item_frames:
            frame_y = songItem.song_interface.song_item.winfo_rooty()
            #medium_height = songItem.song_interface.song_item.winfo_height()/2
            #distance = abs(frame_y + medium_height - y)
            distance = abs(frame_y - y)

            if distance < min_distance:
                min_distance = distance
                index_songItem = songItem.index

        return index_songItem
    
    @classmethod
    def remove_songItems(cls, index):
        if 0 <= index < len(song_item_frames):
            song_item_frames[index].song_interface.destroy()
            del song_item_frames[index]
            cls.reposition_songItems()
    
    @classmethod
    def insert_songItems(cls, index, song):
        if 0 <= index <= len(song_item_frames):
            songItem = SongItem(scrollist, song, index)
            song_item_frames.insert(index, songItem)
            cls.reposition_songItems()
    
    @classmethod
    def reposition_songItems(cls):
        for i, songItem in enumerate(song_item_frames):
            songItem.index = i
            songItem.song_interface.song_item.pack_forget()
        for songItem in song_item_frames:
            songItem.song_interface.song_item.pack(pady=0.5)
    
    @classmethod
    def update_indexControl(cls):
        for i, songItem in enumerate(song_item_frames):
            songItem.indexControl = i


# add_song(Song("1s8tP3jP4GZcyHDsjvw218", "93 Million Miles", "Jason Jackson", "pop", 2012, 68, 3725000))
# add_song(Song("7BRCa8MPiyuvr2VU3O9W0F", "Do Not Let Me Go", "Joshua Jovi", "rock", 2002, 68, 2725000))
# add_song(Song("6nXIYClvJAfi6ujLiKqEq8", "Sky's Still Blue", "Andrew Mraz", "acoustic", 2012, 68, 240166))
# add_song(Song("24NvptbNKGs6sPy1Vh1O0v", "What They Say", "Chris Jackson", "pop", 2012, 68, 3725000))
# add_song(Song("0BP7hSvLAG3URGrEvNNbGM", "Walking in a Winter Wonderland", "Matt Jovi", "rock", 2002, 68, 2725000))
# add_song(Song("3Y6BuzQCg9p4yH347Nn8OW", "Dancing Shoes", "Green de Arco", "rock", 2002, 68, 2725000))

# current = my_song_list.head
# for _ in range(my_song_list.size):
#     song_item_frames.append(SongItem(scrollist, current.song, len(song_item_frames)))
#     current = current.next


# Lectura del .csv
archivo_csv = open('BaseDatos/spotify_data.csv', encoding='utf-8')
archivo = csv.reader(archivo_csv, delimiter=',')
next(archivo)
trie = Trie()


for fila in archivo:
    song = Song(fila[3], fila[2], fila[1], fila[6], fila[5], fila[4], fila[18])
    trie.insert(song.getSong_name(), song)
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
    global general_song
    selectedItem = tree.focus()  # El ítem seleccionado en la tabla
    if selectedItem:
        itemValuesSong = tree.item(selectedItem, 'values')  # Valores de la fila seleccionada
        window.selectedSong = arrSongsCoincidence[int(itemValuesSong[0]) - 1]
        general_song = window.selectedSong
        print(f"Canción seleccionada: {window.selectedSong}")  # Objeto Song
        print(window.selectedSong.getSong_id())  # song_id

def onDoubleClickSong(event):
    global arrSongsCoincidence
    selectedItem = tree.focus()
    if selectedItem:
        itemValuesSong = tree.item(selectedItem, 'values')
        window.selectedSong = arrSongsCoincidence[int(itemValuesSong[0]) - 1]
        print(f"Doble clic en la canción: {window.selectedSong}")
        print(window.selectedSong.getSong_id())

def buttonClick():
    if hasattr(window, 'selectedSong') and window.selectedSong:
        print(f"Retornando el objeto Song: {window.selectedSong}")
        return window.selectedSong
    else:
        print("No se ha seleccionado ninguna canción.")

# Configuración de la interfaz gráfica

main = CTkFrame(window, fg_color="#1e1e1e",  width=700, height=500)  
main.pack(fill="both", expand=True, padx=10, pady=10)

input_frame = CTkFrame(main, fg_color="#1e1e1e")
input_frame.pack(pady=10)

CTkLabel(input_frame, text="Nombre de canción:", text_color="#ffffff").grid(row=0, column=0, padx=5, pady=5)
textbox = CTkTextbox(input_frame, width=150, height=30, fg_color="#2e2e2e", text_color="#ffffff")
textbox.grid(row=0, column=1, padx=5, pady=5)

CTkLabel(input_frame, text="Autor:", text_color="#ffffff").grid(row=0, column=2, padx=5, pady=5)
authorbox = CTkTextbox(input_frame, width=150, height=30, fg_color="#2e2e2e", text_color="#ffffff")
authorbox.grid(row=0, column=3, padx=5, pady=5)

CTkLabel(input_frame, text="Año:", text_color="#ffffff").grid(row=0, column=4, padx=5, pady=5)
yearbox = CTkTextbox(input_frame, width=50, height=30, fg_color="#2e2e2e", text_color="#ffffff")
yearbox.grid(row=0, column=5, padx=5, pady=5)

button = CTkButton(main, text="Buscar", command=getText, fg_color="#5a5a5a", hover_color="#3a3a3a", text_color="#ffffff")
button.pack(pady=10)
button = CTkButton(main, text="Agregar", command=add_new_song, fg_color="#5a5a5a", hover_color="#3a3a3a", text_color="#ffffff")
button.pack(pady=10)

table = CTkFrame(main, fg_color="#1e1e1e")
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

window.mainloop()