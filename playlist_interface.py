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

window.mainloop()