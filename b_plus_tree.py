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


class LeafBPlusTree(NodeBPlusTree):

    def __init__(self) -> None:
        pass


class BPlusTree(object):

    def __init__(self) -> None:
        pass