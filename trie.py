class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False
        self.data = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    