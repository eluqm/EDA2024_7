class Song:
    def __init__(self, song_id, song_name, author, genre, year, popularity, duration):
        self.song_id = song_id
        self.song_name = song_name
        self.author = author
        self.genre = genre
        self.year = year
        self.popularity = popularity
        self.duration = self.convertTime(duration)
        
    def convertTime(self, miliSeconds):
        total_seconds = miliSeconds // 1000 # Dividiendo para obtener un entero
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes}:{seconds:02d}" # 02d para usar dos digitos y de ser un digito completa con cero adelante
        
        
    def __str__(self):
        return f"{self.song_name}, {self.author}, {self.year}, {self.duration}"
        
cancion = Song("53QF56cjZA9RTuuMZDrSA6","I Won't Give Up","Jason Mraz,I Won't Give Up", "acoustic", 2012, 68, 240166)
print(cancion)