import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import tempfile
import os
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pygame import mixer

class MusicPlayer(ctk.CTk):
    def __init__(self, spotify_id):
        super().__init__()
        
        self.spotify_id = spotify_id
        self.volume = 0.5  # Volumen inicial (rango de 0 a 1)
        self.paused = False

        self.title("Reproductor de Música")
        self.geometry("400x200")

        # Inicializar pygame mixer
        mixer.init()

        # Crear widgets
        self.create_widgets()
        
        # Reproducir la canción
        self.reproducir_cancion()

    def create_widgets(self):
        self.pause_button = ctk.CTkButton(self, text="Pausa", command=self.toggle_pause)
        self.pause_button.pack(pady=10)

        self.vol_up_button = ctk.CTkButton(self, text="+", command=self.vol_up)
        self.vol_up_button.pack(pady=10)

        self.vol_down_button = ctk.CTkButton(self, text="-", command=self.vol_down)
        self.vol_down_button.pack(pady=10)

        self.volume_label = ctk.CTkLabel(self, text=f"Volumen: {int(self.volume * 100)}%")
        self.volume_label.pack(pady=10)

    def reproducir_cancion(self):
        try:
            # Configurar el cliente de Spotify con la autenticación OAuth
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='06e5f880929843ae94307601ad4f66df',
                                                           client_secret='43e716bdc45d4b789e576840be632adb',
                                                           redirect_uri='http://localhost:8080',
                                                           scope='user-library-read user-read-playback-state streaming'))

            # Obtener información de la pista desde Spotify
            track = sp.track(self.spotify_id)
            preview_url = track['preview_url']  # URL de previsualización de la canción en Spotify

            if preview_url:
                print(f"URL de previsualización encontrada: {preview_url}")

                # Descargar la canción temporalmente
                temp_file = tempfile.NamedTemporaryFile(delete=False)
                with requests.get(preview_url, stream=True) as r:
                    r.raise_for_status()
                    for chunk in r.iter_content(chunk_size=8192):
                        temp_file.write(chunk)
                temp_file.close()

                mixer.music.load(temp_file.name)
                mixer.music.set_volume(self.volume)
                mixer.music.play()

                print("Reproduciendo canción...")

                self.after(1000, self.check_music_end)  # Verificar el final de la canción

            else:
                print(f"No se pudo reproducir la canción con ID {self.spotify_id}. No hay URL de previsualización disponible.")
        except Exception as e:
            print(f"Error al reproducir la canción: {e}")

    def toggle_pause(self):
        if self.paused:
            mixer.music.unpause()
            self.pause_button.configure(text="Pausa")
            self.paused = False
            print("Reanudando canción...")
        else:
            mixer.music.pause()
            self.pause_button.configure(text="Reanudar")
            self.paused = True
            print("Pausando canción...")

    def vol_up(self):
        self.volume = min(1.0, self.volume + 0.1)
        mixer.music.set_volume(self.volume)
        self.volume_label.configure(text=f"Volumen: {int(self.volume * 100)}%")
        print(f"Volumen aumentado: {self.volume}")

    def vol_down(self):
        self.volume = max(0.0, self.volume - 0.1)
        mixer.music.set_volume(self.volume)
        self.volume_label.configure(text=f"Volumen: {int(self.volume * 100)}%")
        print(f"Volumen disminuido: {self.volume}")

    def check_music_end(self):
        if not mixer.music.get_busy() and not self.paused:
            mixer.music.stop()
            print("Canción terminada.")
        else:
            self.after(1000, self.check_music_end)

if __name__ == "__main__":
    # Reemplaza '53QF56cjZA9RTuuMZDrSA6' con el ID de la canción que deseas reproducir desde Spotify
    spotify_id = '69uxyAqqPIsUyTO8txoP2M'
    player = MusicPlayer(spotify_id)
    player.mainloop()
