from customtkinter import *
from tkinter import *
from PIL import Image

class DragDropListbox(Listbox):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bind('<Button-1>', self.save_mouse_position)
        self.bind('<B1-Motion>', self.on_drag)

        self.drag_data = {"x": 0, "y": 0, "item": None}

    def save_mouse_position(self, event):
        pass

    def on_drag(self, event):
        pass

window = CTk()
window.title("Music Player")
window.geometry("850x500")
window.configure(fg_color='black')
set_appearance_mode("darck")

default_icon_data = Image.open("src/default-icon.jpeg")
default_icon = CTkImage(dark_image=default_icon_data, light_image=default_icon_data, size=(200, 200))
home_icon_data = Image.open("src/home-icon.png")
home_icon = CTkImage(dark_image=home_icon_data, light_image=home_icon_data, size=(40, 40))
loupe_icon_data = Image.open("src/loupe-icon.png")
loupe_icon = CTkImage(dark_image=loupe_icon_data, light_image=loupe_icon_data, size=(40, 40))


menu = CTkFrame(master=window, width=75, height=500, fg_color="#272727", corner_radius=0)
menu.pack(expand=True, side="left")

button_home = CTkButton(master=menu, text="", width=40, height=40, fg_color="#272727", image=home_icon, command=lambda: print("Ventana Principal"))
button_home.place(relx=0.5, rely=0.1, anchor="center")
button_search = CTkButton(master=menu, text="", width=40, height=40, fg_color="#272727", image=loupe_icon, command=lambda: print("Ventana Buscar"))
button_search.place(relx=0.5, rely=0.24, anchor="center")


player = CTkFrame(master=window, width=375, height=500, fg_color="#000000", corner_radius=0)
player.pack(expand=True, side="left")

CTkLabel(master=player, text="", image=default_icon).place(relx=0.5, rely=0.3, anchor="center")
CTkLabel(master=player, text="Nombre canción", text_color="#ffffff", font=("Arial Bold", 24)).place(relx=0.5, rely=0.6, anchor="center")
CTkLabel(master=player, text="Artista", text_color="#ffffff", font=("Arial Bold", 16)).place(relx=0.5, rely=0.7, anchor="center")
slider = CTkSlider(master=player, from_=0, to=100, number_of_steps=5, button_color="#C850C0", progress_color="#C850C0").place(relx=0.5, rely=0.8, anchor="center")


playlist = CTkScrollableFrame(master=window, width=380, height=450, fg_color="#272727", corner_radius=0,)
playlist.pack(expand=True, side="right", pady=(30, 20), padx=(0, 20))

list = DragDropListbox(playlist, bg="#272727", fg="black",  selectbackground="blue", selectforeground="white", highlightthickness=0,) #bd=0)
list.pack(expand=True, fill=BOTH)


window.mainloop()