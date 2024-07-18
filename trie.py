from song import Song
import dill as pickle

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False
        self.data = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, data):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endWord = True
        if data is not None:
            node.data.append(data)
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.endWord
    # Se puede resumir este con getSong
            
    def getSong(self, word):
        if self.search(word):
            node = self.root
            for char in word:
                node = node.children[char]
            if node.endWord:
                dats = []
                for dat in node.data:
                    dats.append(dat)
                return dats
        return []
    # Tiempo O(n)
    
    def getSong(self, songName, author):
        if self.search(songName):
            node = self.root
            for char in songName:
                node = node.children[char]
            if node.endWord:
                for dat in node.data:
                    if dat.author == author:
                        return dat
        return
        
    def contains(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        
    def saveFile(self, file):
        with open(file, 'wb') as f:
            pickle.dump(self, f)
            
    def loadFile(self, file):
        with open(file, 'rb') as f:
            return pickle.load(f)

"""    
cancion = Song("53QF56cjZA9RTuuMZDrSA6","I Won't Give Up","Jason Mraz", "acoustic", 2012, 68, 240166)
print(cancion)
cancion1 = Song("53QF56cjZA9RTuuMZDrS44","I Won't Give Up","Michael Jackson", "pop", 2012, 68, 3725000)
print(cancion1)
cancion2 = Song("ghtF56cjZA9RTuuMZDrSA6","Its my live","Bon Jovi", "rock", 2002, 68, 2725000)
print(cancion2)

rep = Trie()
rep.insert(cancion.getSong_name(), cancion)
rep.insert(cancion1.getSong_name(), cancion1)
rep.insert(cancion2.getSong_name(), cancion2)

print(rep.getSong("I Won't Give Up"))
"""