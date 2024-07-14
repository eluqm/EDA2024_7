class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add_song(self, song):
        new_node = Node(song)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = tail
            tail = new_node
        self.size += 1