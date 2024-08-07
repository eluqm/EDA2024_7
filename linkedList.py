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
    
    def add_song_at_position(self, song, position):
        if position < 0 or position > self.size:
            raise IndexError("Invalid position")

        new_node = Node(song)
        if position == 0:
            if not self.head:
                self.head = new_node
                self.tail = new_node
                self.head.prev = self.head
                self.head.next = self.head
            else:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.head = new_node
        elif position == self.size:
            self.add_song(song)
        else:
            current = self.head
            for _ in range(position):
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node

        self.size += 1
    
    def remove_song(self, song):
        if self.head:
            current = self.head
            for _ in range(self.size):
                if current.song == song:
                    if self.size == 1:
                        self.head = None
                        self.tail = None
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        if current == self.head:
                            self.head = current.next
                        if current == self.tail:
                            self.tail = current.prev
                    self.size -= 1
                    return True
                current = current.next
        return False
    
    def change_order(self, current_position, new_position):
        if current_position < 0 or current_position >= self.size or new_position < 0 or new_position >= self.size:
            return False
        if current_position == new_position:
            return True

        current = self.head
        for _ in range(current_position):
            current = current.next

        current.prev.next = current.next
        current.next.prev = current.prev

        if current == self.head:
            self.head = current.next
        if current == self.tail:
            self.tail = current.prev

        new_current = self.head
        for _ in range(new_position):
            new_current = new_current.next

        if new_position == 0:
            current.next = self.head
            current.prev = self.tail
            self.head.prev = current
            self.tail.next = current
            self.head = current
        else:
            current.next = new_current
            current.prev = new_current.prev
            new_current.prev.next = current
            new_current.prev = current
        
        self.tail = self.head.prev
        return True

    # optimizar O(n^2)
    def random_play(self):
        import random
        random_playlist = LinkedList()
        current = self.head
        for _ in range(self.size):
            num_random = random.randint(0, random_playlist.size)
            random_playlist.add_song_at_position(current.song, num_random)
            current = current.next
        return random_playlist
    
    def print(self):
        current = self.head
        for _ in range(self.size):
            print(current.song)
            current = current.next