class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0