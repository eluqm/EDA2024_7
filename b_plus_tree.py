# import random

class NodeBPlusTree(object):

    def __init__(self, parent=None):
        self.keys: list = []
        self.values: list[NodeBPlusTree] = []
        self.parent: NodeBPlusTree = parent

    def index(self, key):
        for i, item in enumerate(self.keys):
            if key < item:
                return i
        return len(self.keys)

    def __getitem__(self, item):
        return self.values[self.index(item)]
    
    def __setitem__(self, key, value):
        i = self.index(key)
        self.keys[i:i] = key
        if i < len(self.values):
            self.values.pop(i)
        self.values[i:i] = value

    def __delitem__(self, key):
        i = self.index(key)
        del self.values[i]
        del self.keys[i]

    def split(self):
        global splits, parent_splits
        splits += 1
        parent_splits += 1
        
        left = NodeBPlusTree(self.parent)
        
        mid = len(self.keys) // 2

        left.keys = self.keys[:mid]
        left.values = self.values[:mid + 1]
        
        for child in left.values:
            child.parent = left
        
        key = self.keys[mid]
        self.keys = self.keys[mid + 1:]
        self.values = self .values[mid + 1:]

    def fusion():
        pass

    def borrow_key():
        pass

class LeafBPlusTree(NodeBPlusTree):

    def __init__(self, parent=None, prev_node=None, next_node=None):
        super(LeafBPlusTree, self)._init_(parent)
        self.next: LeafBPlusTree = next_node
        if next_node is not None:
            next_node.pref = self
        self.prev: LeafBPlusTree = prev_node
        if prev_node is not None:
            prev_node.next = self

    def __getitem__(self, item):
        return self.values[self.keys.index(item)]

    def __setitem__(self, key, value):
            i = self.index(key)
            if key not in self.keys:
                self.keys[i:i] = [key]
                self.values[i:i] = [value]
            else:
                self.values[i - 1] = value

    def __delitem__(self, key):
        i = self.keys.index(key)
        del self.keys[i]
        del self.values[i]

    def fusion():
        pass

    def borrow_key():
        pass



class BPlusTree(object):

    MAXIMUM = 4
    root: NodeBPlusTree

    def __init__(self, maximum = MAXIMUM):
        self.root = LeafBPlusTree()
        self.maximum: int = maximum if maximum > 2 else 2
        self.minimum: int = self.maximum // 2
        self.depth = 0

    def __getitem__():
        pass

    def __setitem():
        pass

    def find():
        pass

    def query():
        pass

    def change():
        pass

    def insert():
        pass

    def insert_index():
        pass

    def delete():
        pass