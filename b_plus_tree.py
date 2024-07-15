import random

class NodeBPlusTree(object):

    def __init__(self, parent=None):
        self.keys: list = []
        self.values: list[NodeBPlusTree] = []
        self.parent: NodeBPlusTree = parent


class LeafBPlusTree(NodeBPlusTree):

    def __init__(self) -> None:
        pass


class BPlusTree(object):

    def __init__(self) -> None:
        pass