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

song_item = CTkFrame(master=playlist, width=380, height=50, fg_color="#000000", corner_radius=0)
song_item.pack(pady=1)

# Imagen
icon_song_data = Image.open("src/default-icon.jpeg")
icon_song = CTkImage(dark_image=icon_song_data, light_image=icon_song_data, size=(40, 40))
CTkLabel(master=song_item, text="", image=icon_song).pack(side="left", pady=(5, 5), padx=(5, 5))
# Datos de la cancion
specifications = CTkFrame(master=song_item, width=210, height=50, fg_color="#000000", corner_radius=0)
specifications.pack(side="left", padx=(0, 0))
song_name = CTkLabel(master=specifications, text="Nombre de la cancion", text_color="#ffffff", font=("Arial Bold", 15), width=210, height=30, anchor="w")
song_name.pack(pady=(0, 0))
song_data = CTkLabel(master=specifications, text="Autor · N° vistas", text_color="#ffffff", font=("Arial Bold", 10), width=210, height=20, anchor="w")
song_data.pack(pady=(0, 0))


window.mainloop()