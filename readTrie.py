from trie import Trie
from joblib import dump, load

trie = Trie.loadFile('BaseDatos/trieSongName.bin')

print(trie.getSong("Hello"))