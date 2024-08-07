from customtkinter import *
from tkinter import *
from PIL import Image
from song import Song
from linkedList import LinkedList

window = CTk()
window.title("Music Player")
window.geometry("850x500")
window.configure(fg_color='black')

playlist = CTkScrollableFrame(master=window, width=380, height=450, fg_color="#272727", corner_radius=0,)
playlist.pack(expand=True, side="right", pady=(30, 20), padx=(0, 20))

ctk_frames = [] #cambiar nombre
my_song_list = LinkedList()

class SongItem_Interface:
    def __init__(self, list, song):
        self.song = song

        # Elemento cancion
        self.song_item = CTkFrame(master=list, width=380, height=50, fg_color="#000000", corner_radius=0)
        self.song_item.pack(pady=1)

        # Imagen
        self.icon_song_data = Image.open("src/default-icon.jpeg")
        self.icon_song = CTkImage(dark_image=self.icon_song_data, light_image=self.icon_song_data, size=(40, 40))
        CTkLabel(master=self.song_item, text="", image=self.icon_song).pack(side="left", pady=(5, 5), padx=(5, 5))
        # Datos de la cancion
        self.specifications = CTkFrame(master=self.song_item, width=210, height=50, fg_color="#000000", corner_radius=0)
        self.specifications.pack(side="left", padx=(0, 0))
        self.song_name = CTkLabel(master=self.specifications, text=self.song.getSong_name(), text_color="#ffffff", font=("Arial Bold", 15), width=210, height=30, anchor="w")
        self.song_name.pack(pady=(0, 0))
        self.song_data = CTkLabel(master=self.specifications, text=self.song.getAuthor(), text_color="#ffffff", font=("Arial Bold", 10), width=210, height=20, anchor="w")
        self.song_data.pack(pady=(0, 0))
        # Duracion
        self.duration = CTkLabel(master=self.song_item, text=self.song.getDuration(), text_color="#ffffff", font=("Arial Bold", 10), width=60, height=20, anchor="e")
        self.duration.pack(side="left", pady=(30, 0), padx=(5, 5))
        # Boton de movimiento
        self.position = CTkFrame(master=self.song_item, width=60, height=50, fg_color="#000000", corner_radius=0)
        self.position.pack(side="left", padx=(0, 0))
        self.icon_position_data = Image.open("src/position-icon.png")
        self.icon_position = CTkImage(dark_image=self.icon_position_data, light_image=self.icon_position_data, size=(30, 10))
        self.button_position = CTkButton(master=self.position, text="", width=30, height=16, fg_color="#000000", image=self.icon_position)
        self.button_position.place(relx=0.5, rely=0.5, anchor="center")

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
            my_song_list.change_order(self.indexControl, new_index)
            SongItem.update_indexControl()
    
    def move_item(self, from_index, to_index):
        if from_index == to_index:
            return

        item = ctk_frames.pop(from_index)
        ctk_frames.insert(to_index, item)

        SongItem.reposition_songItems()

    def nearest_songItem(self, y):
        index_songItem = None
        min_distance = float('inf')

        for songItem in ctk_frames:
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
        if 0 <= index < len(ctk_frames):
            ctk_frames[index].song_interface.destroy()
            del ctk_frames[index]
            cls.reposition_songItems()
    
    @classmethod
    def insert_songItems(cls, index, song):
        if 0 <= index <= len(ctk_frames):
            songItem = SongItem(playlist, song, index)
            ctk_frames.insert(index, songItem)
            cls.reposition_songItems()
    
    @classmethod
    def reposition_songItems(cls):
        for i, songItem in enumerate(ctk_frames):
            songItem.index = i
            songItem.song_interface.song_item.pack_forget()
        for songItem in ctk_frames:
            songItem.song_interface.song_item.pack(pady=1)
    
    @classmethod
    def update_indexControl(cls):
        for i, songItem in enumerate(ctk_frames):
            songItem.indexControl = i

my_song_list.add_song(Song("53QF56cjZA9RTuuMZDrSA6", "I Won't Give Up", "Jason Mraz", "acoustic", 2012, 68, 240166))
my_song_list.add_song(Song("53QF56cjZA9RTuuMZDrS44", "Red Hood", "Michael Jackson", "pop", 2012, 68, 3725000))
my_song_list.add_song(Song("ghtF56cjZA9RTuuMZDrSA6", "Its my live", "Bon Jovi", "rock", 2002, 68, 2725000))
my_song_list.add_song(Song("ghtF56cjZA9RTuuMZDrSA6", "Y will survive", "Juana de Arco", "rock", 2002, 68, 2725000))
my_song_list.add_song(Song("53QF56cjZA9RTuuMZDrSA6", "I Won't Give Up", "Jason Mraz", "acoustic", 2012, 68, 240166))
my_song_list.add_song(Song("53QF56cjZA9RTuuMZDrS44", "Red Hood", "Michael Jackson", "pop", 2012, 68, 3725000))
my_song_list.add_song(Song("ghtF56cjZA9RTuuMZDrSA6", "Its my live", "Bon Jovi", "rock", 2002, 68, 2725000))
my_song_list.add_song(Song("ghtF56cjZA9RTuuMZDrSA6", "Y will survive", "Juana de Arco", "rock", 2002, 68, 2725000))
my_song_list.add_song(Song("53QF56cjZA9RTuuMZDrSA6", "I Won't Give Up", "Jason Mraz", "acoustic", 2012, 68, 240166))

current = my_song_list.head
for _ in range(my_song_list.size):
    ctk_frames.append(SongItem(playlist, current.song, len(ctk_frames)))
    current = current.next

def mostrar():
    my_song_list.print()
    for songItem in ctk_frames:
        print(songItem)

bug = CTkButton(master=window, text="mostrar", width=30, height=16, fg_color="#ffffff", command=mostrar)
bug.place(relx=0.1, rely=0.5, anchor="center")

window.mainloop()