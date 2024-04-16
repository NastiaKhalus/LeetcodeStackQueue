"""functions for queue"""
class Node:
    """created new class"""
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:
    """created new class"""
    def __init__(self):
        self.head = None
    def is_empty(self):
        """empty"""
        return self.head is None
    def push(self, item):
        """push"""
        self.head = Node(item, self.head)
    def pop(self):
        """pop"""
        item = self.head.item
        self.head = self.head.next
        return item

    @property
    def peek(self):
        """peek"""
        return self.head.item

class MyQueue:
    """created new class"""
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        """push"""
        self.s1.push(x)

    def pop(self):
        """pop"""
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        """peek"""
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.peek

    def empty(self):
        """empty"""
        return self.s1.is_empty() and self.s2.is_empty()
