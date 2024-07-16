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

    def fusion(self):
        global fusions, parent_fusions
        fusions += 1
        parent_fusions += 1
        index = self.parent.index(self.keys[0])

        if index < len(self.parent.keys):
            next_node: NodeBPlusTree = self.parent.values[index + 1]
            next_node.keys[0:0] = self.keys + [self.parent.keys[index]]
            for child in self.values:
                child.parent = next_node
            next_node.values[0:0] = self.values
        else:
            prev: NodeBPlusTree = self.parent.values[-2]
            prev.keys += [self.parent.keys[-1]] + self.keys
            for child in self.values:
                child.parent = prev
            prev.values += self.values

    def borrow_key(self, minimum: int):
        index = self.parent.index(self.keys[0])
        if index < len(self.parent.keys):
            next_node: NodeBPlusTree = self.parent.values[index + 1]
            if len(next_node.keys) > minimum:
                self.keys += [self.parent.keys[index]]

                borrow_node = next_node.values.pop(0)
                borrow_node.parent = self
                self.values += [borrow_node]
                self.parent.keys[index] = next_node.keys.pop(0)
                return True
        elif index != 0:
            prev: NodeBPlusTree = self.parent.values[index - 1]
            if len(prev.keys) > minimum:
                self.keys[0:0] = [self.parent.keys[index - 1]]

                borrow_node = prev.values.pop()
                borrow_node.parent = self
                self.values[0:0] = [borrow_node]
                self.parent.keys[index - 1] = prev.keys.pop()
                return True
        return False

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

    def split(self):
        global splits
        splits += 1

        left = LeafBPlusTree(self.parent, self.prev, self)
        mid = len(self.keys) // 2
        
        left.keys = self.keys[:mid]
        left.values = self.values[:mid]

        self.keys: list = self.keys[mid:]
        self.values: list = self.values[mid:]

        return self.keys[0], [left, self]
    
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