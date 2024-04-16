"""classes"""
class Node:
    """created new class"""
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Queue:
    """created new class"""
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        """empty"""
        return self.head is None

    def add(self, item):
        """add"""
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        """pop"""
        if self.head:
            item = self.head
            self.head = self.head.next
            return item

    @property
    def peek(self):
        """peek"""
        return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

class MyStack:
    """created new class"""
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        """push"""
        self.q1.add(x)
        while not self.q2.is_empty():
            self.q1.add(self.q2.pop().item)
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """pop"""
        return self.q2.pop().item

    def top(self):
        """top"""
        return self.q2.peek

    def empty(self):
        """empty"""
        return self.q2.is_empty()
