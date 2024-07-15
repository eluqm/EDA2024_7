from customtkinter import *
from PIL import Image

window = CTk()
window.title("Music Player")
window.geometry("900x500")

default_logo_data = Image.open("src/default-logo.jpeg")
default_logo = CTkImage(dark_image=default_logo_data, light_image=default_logo_data, size=(200, 200))

player = CTkFrame(master=window, width=450, height=500, fg_color="#42214b", corner_radius=0)
player.pack(expand=True, side="left")

CTkLabel(master=player, text="", image=default_logo).place(relx=0.5, rely=0.3, anchor="center")
CTkLabel(master=player, text="Nombre canción", text_color="#010c1e", font=("Arial Bold", 24)).place(relx=0.5, rely=0.6, anchor="center")
CTkLabel(master=player, text="Artista", text_color="#7E7E7E", font=("Arial Bold", 16)).place(relx=0.5, rely=0.7, anchor="center")
slider = CTkSlider(master=player, from_=0, to=100, number_of_steps=5, button_color="#C850C0", progress_color="#C850C0").place(relx=0.5, rely=0.8, anchor="center")

list = CTkFrame(master=window, width=450, height=500, fg_color="#8D4F3A", corner_radius=0)
list.pack(expand=True, side="right")
window.mainloop()