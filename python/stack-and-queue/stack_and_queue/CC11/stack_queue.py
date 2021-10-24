class Node:
    def __init__(self, value, next = None):
        self.value=value
        self.next=next


class Stack():
    def __init__(self):
        self.elements = []
    def push(self, element):
        self.elements.append(element)
    def pop(self):
        return self.elements.pop()
    def is_empty(self):
        return self.elements == []
    def peek():
        if not self.elements.is_empty():
            return self.elements[-1]
    def get_elements(self):
        return self.elements

class PseudoQueue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()
    def is_empty(self):
        return self.stack_1.is_empty() and self.stack_2.is_empty()
    def enqueue(self, item):
        self.stack_1.push(item)
    def dequeue(self):
        if self.stack_2.is_empty():
            while not self.stack_1.is_empty():
                self.stack_2.push(self.stack_1.pop())

        return self.stack_2.pop()

aseel = PseudoQueue()
aseel.enqueue(1)
aseel.enqueue(2)
aseel.enqueue(3)
print(aseel.stack_1.elements)
aseel.enqueue(7)
print(aseel.stack_1.elements)
print(aseel.dequeue())







