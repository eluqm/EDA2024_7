import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pygame
import requests
import tempfile
import os

# Configuración de la ventana pygame
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200

# Colores RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class MusicPlayer:
    def __init__(self, spotify_id):
        self.spotify_id = spotify_id
        self.volume = 0.5  # Volumen inicial (rango de 0 a 1)
        self.paused = False

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

                # Inicializar pygame y configurar la ventana
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(temp_file.name)
                pygame.mixer.music.set_volume(self.volume)
                pygame.mixer.music.play()

                self.create_window()

                # Reproducir la canción
                print("Reproduciendo canción...")

                # Manejar eventos de pygame
                clock = pygame.time.Clock()
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if self.btn_pause_rect.collidepoint(event.pos):
                                if self.paused:
                                    pygame.mixer.music.unpause()
                                    self.paused = False
                                    print("Reanudando canción...")
                                else:
                                    pygame.mixer.music.pause()
                                    self.paused = True
                                    print("Pausando canción...")
                            elif self.btn_vol_up_rect.collidepoint(event.pos):
                                self.volume = min(1.0, self.volume + 0.1)
                                pygame.mixer.music.set_volume(self.volume)
                                print(f"Volumen aumentado: {self.volume}")
                            elif self.btn_vol_down_rect.collidepoint(event.pos):
                                self.volume = max(0.0, self.volume - 0.1)
                                pygame.mixer.music.set_volume(self.volume)
                                print(f"Volumen disminuido: {self.volume}")

                    # Actualizar la ventana
                    self.update_window()

                    # Esperar hasta que termine de reproducirse
                    if not pygame.mixer.music.get_busy() and not self.paused:
                        running = False

                    clock.tick(30)

                pygame.mixer.music.stop()
                pygame.quit()

                # Eliminar el archivo temporal
                os.remove(temp_file.name)

            else:
                print(f"No se pudo reproducir la canción con ID {self.spotify_id}. No hay URL de previsualización disponible.")
        except Exception as e:
            print(f"Error al reproducir la canción: {e}")

    def create_window(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Reproductor de Música')
        self.font = pygame.font.Font(None, 36)

        # Crear botones
        self.btn_pause = pygame.Rect(50, 100, 100, 50)
        self.btn_vol_up = pygame.Rect(200, 50, 50, 50)
        self.btn_vol_down = pygame.Rect(200, 150, 50, 50)

        # Rectángulos para detectar clics en botones
        self.btn_pause_rect = pygame.draw.rect(self.screen, GREEN, self.btn_pause)
        self.btn_vol_up_rect = pygame.draw.rect(self.screen, GREEN, self.btn_vol_up)
        self.btn_vol_down_rect = pygame.draw.rect(self.screen, GREEN, self.btn_vol_down)

    def update_window(self):
        self.screen.fill(WHITE)

        # Dibujar botones
        pygame.draw.rect(self.screen, BLUE, self.btn_pause)
        pygame.draw.rect(self.screen, BLUE, self.btn_vol_up)
        pygame.draw.rect(self.screen, BLUE, self.btn_vol_down)

        # Etiquetas de los botones
        pause_text = self.font.render("Pausa" if not self.paused else "Reanudar", True, WHITE)
        vol_up_text = self.font.render("+", True, WHITE)
        vol_down_text = self.font.render("-", True, WHITE)

        # Posicionar etiquetas de los botones
        self.screen.blit(pause_text, (self.btn_pause.x + 10, self.btn_pause.y + 10))
        self.screen.blit(vol_up_text, (self.btn_vol_up.x + 15, self.btn_vol_up.y + 5))
        self.screen.blit(vol_down_text, (self.btn_vol_down.x + 15, self.btn_vol_down.y + 5))

        # Mostrar información en la ventana
        text = self.font.render(f"Volumen: {int(self.volume * 100)}%", True, BLACK)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, 20))
        self.screen.blit(text, text_rect)

        pygame.display.flip()

if __name__ == "__main__":
    # Reemplaza '53QF56cjZA9RTuuMZDrSA6' con el ID de la canción que deseas reproducir desde Spotify
    spotify_id = '69uxyAqqPIsUyTO8txoP2M'
    player = MusicPlayer(spotify_id)
    player.reproducir_cancion()
