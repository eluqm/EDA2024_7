import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

# Configuración de SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='50f9d9647baf4ad6ab9047f8431a2b63',
                                               client_secret='7a99540fc7804778bec90a6489b02927',
                                               redirect_uri='http://localhost:8080',
                                               scope='user-library-read user-read-playback-state streaming'))

try:
    # Obtén el token de acceso
    token_info = sp.auth_manager.get_access_token(as_dict=True)
    print("Token de acceso:", token_info)

    headers = {
        'Authorization': f'Bearer {token_info["access_token"]}',
    }

    try:
        # Realiza una solicitud a la API de Spotify para obtener información del usuario
        response = requests.get('https://api.spotify.com/v1/me', headers=headers)
        response.raise_for_status()  # Lanza una excepción para respuestas de error HTTP
        print("Respuesta de la API (usuario):", response.json())

        # También prueba con otra pista para verificar el acceso
        track_id = '3Egxk5yd9Y71KsE4h8dCLU'  # Cambia a un ID válido
        response = requests.get(f'https://api.spotify.com/v1/tracks/{track_id}', headers=headers)
        response.raise_for_status()  # Lanza una excepción para respuestas de error HTTP
        print("Respuesta de la API (pista):", response.json())
        
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except Exception as err:
        print(f"Otro error: {err}")
except spotipy.exceptions.SpotifyOauthError as oauth_err:
    print(f"Error de OAuth: {oauth_err}")
except Exception as err:
    print(f"Otro error: {err}")
