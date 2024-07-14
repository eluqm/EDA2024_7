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
            self.head.prev = self.head
            self.head.next = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
        self.size += 1
    
    def remove_song(self, song):
        if self.head:
            current = self.head
            for _ in range(self.size):
                if current.song == song:
                    if self.size == 1:
                        self.head = None
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        if current == self.head:
                            self.head = current.next
                    self.size -= 1
                    return True
                current = current.next
        return False