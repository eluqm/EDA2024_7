from song import Song

splits = 0
parent_splits = 0
fusions = 0
parent_fusions = 0

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
        self.keys[i:i] = [key]
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

        return key, [left, self]

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
        super(LeafBPlusTree, self).__init__(parent)
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
            # if key not in self.keys:
            self.keys[i:i] = [key]
            self.values[i:i] = [value]
            # else:
            #     self.values[i - 1] = value

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
    
    def fusion(self):
        global fusions
        fusions += 1

        if self.next is not None and self.next.parent == self.parent:
            self.next.keys[0:0] = self.keys
            self.next.values[0:0] = self.values
        else:
            self.prev.keys += self.keys
            self.prev.values += self.values

        if self.next is not None:
            self.next.prev = self.prev
        if self.prev is not None:
            self.prev.next = self.next

    def borrow_key(self, minimum: int):
        index = self.parent.index(self.keys[0])
        if index < len(self.parent.keys) and len(self.next.keys) > minimum:
            self.keys += [self.next.keys.pop(0)]
            self.values += [self.next.values.pop(0)]
            self.parent.keys[index] = self.next.keys[0]
            return True
        elif index != 0 and len(self.prev.keys) > minimum:
            self.keys[0:0] = [self.prev.keys.pop()]
            self.values[0:0] = [self.prev.values.pop()]
            self.parent.keys[index - 1] = self.keys[0]
            return True
        return False

class BPlusTree(object):

    MAXIMUM = 4
    root: NodeBPlusTree

    def __init__(self, maximum = MAXIMUM):
        self.root = LeafBPlusTree()
        self.maximum: int = maximum if maximum > 2 else 2
        self.minimum: int = self.maximum // 2
        self.depth = 0

    def __getitem__(self, item):
        return self.find(item)[item]

    def __setitem__(self, key, value, leaf=None):
        if leaf is None:
            leaf = self.find(key)
        leaf[key] = value
        if len(leaf.keys) > self.maximum:
            self.insert_index(*leaf.split())

    def find(self, key) -> LeafBPlusTree:
        node = self.root

        while type(node) is not LeafBPlusTree:
            node = node[key]

        return node

    def query(self, key):
        leaf = self.find(key)
        return leaf[key] if key in leaf.keys else None

    def change(self, key, value):
        leaf = self.find(key)
        if key not in leaf.keys:
            return False, leaf
        else:
            leaf[key] = value
            return True, leaf

    def insert(self, key, value):
        leaf = self.find(key)
        # if key in leaf.keys:
        #     return False, leaf
        # else:
        self.__setitem__(key, value, leaf)
        return True, leaf

    def insert_index(self,key, values: list[NodeBPlusTree]):
        parent = values[1].parent
        if parent is None:
            values[0].parent = values[1].parent = self.root = NodeBPlusTree()
            self.depth += 1
            self.root.keys = [key]
            self.root.values = values
            return
        
        parent[key] = values

        if len(parent.keys) > self.maximum:
            self.insert_index(*parent.split())

    def delete(self, key, node: NodeBPlusTree = None):
        if node is None:
            node = self.find(key)
        del node[key]

        if len(node.keys) > self.maximum:
            if node == self.root:
                if len(self.root.keys) == 0 and len(self.root.values) > 0:
                    self.root = self.root.values[0]
                    self.root.parent = None
                    self.depth -= 1
                return
            elif not node.borrow_key(self.minimum):
                node.fusion()
                self.delete(key, node.parent)

    def first(self):
        leaf = self.leftmost_leaf()
        if leaf.keys:
            return leaf.keys[0], leaf.values[0]
        else:
            return None, None
        
    def search(self, key):
        # Comienza en el nodo raíz
        current_node = self.root
        
        # Recorre los nodos internos hasta llegar a una hoja
        while not isinstance(current_node, LeafBPlusTree):
            # Encuentra el índice del primer valor que es mayor o igual que la clave de búsqueda
            index = current_node.index(key)
            # Avanza al hijo correspondiente
            current_node = current_node.values[index]
        
        # En el nodo hoja, busca la clave
        if key in current_node.keys:
            return current_node[key]
        return None

    def show(self, node=None, file=None, _prefix="", _last=True):
        if node is None:
            node = self.root
        print(_prefix, "`- " if _last else "|- ", node.keys, sep="", file=file)
        _prefix += "   " if _last else "|  "

        if type(node) is NodeBPlusTree:
            for i, child in enumerate(node.values):
                _last = (i == len(node.values) - 1)
                self.show(child, file, _prefix, _last)

    def output(self):
        return splits, parent_splits, fusions, parent_fusions, self.depth

    def readfile(self, reader):
        i = 0
        for i, line in enumerate(reader):
            s = line.split(',')
            if len(s) > 1:
                song = Song(s[0], s[1], s[2], s[3])
                self.insert(song.title, song)
        return i

    def writefile(self, file):
        with open(file, 'w') as f:
            def write_node(node, depth):
                for i, key in enumerate(node.keys):
                    if type(node) is LeafBPlusTree:
                        f.write(f'{key.title},{key.artist},{key.album},{key.year}\n')
                    else:
                        write_node(node.values[i], depth + 1)
                if not type(node) is LeafBPlusTree:
                    write_node(node.values[-1], depth + 1)
            write_node(self.root, 0)