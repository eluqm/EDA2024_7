class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False
        self.data = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, data)
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endWord = True
        if data is not None:
            node.data.append(info)
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children[]
                return False, []
            node = node.children[char]
        if node.endWord:
            return True, node.data
        else:
            return False, []
        
    