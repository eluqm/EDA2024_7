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
        self.duration = CTkLabel(master=self.song_item, text=self.song.getDuration(), text_color="#ffffff", font=("Arial Bold", 10), width=60, height=10, anchor="e")
        self.duration.pack(side="left", pady=(34, 0), padx=(5, 5))
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
        self.indexOriginal = index
        self.song_interface = SongItem_Interface(list, song)
        self.song_interface.button_position.bind('<Button-1>', self.save_mouse_position)
        self.song_interface.button_position.bind('<B1-Motion>', self.on_drag)
        self.song_interface.button_position.bind('<ButtonRelease-1>', self.on_button_release)
        self.drag_data = {"x": 0, "y": 0, "item": None}
    
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

window.mainloop()