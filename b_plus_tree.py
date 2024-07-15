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

class BPlusTree(object):

    def __init__(self) -> None:
        pass