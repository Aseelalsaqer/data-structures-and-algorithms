
from stack_and_queue.stack import Stack


class MaxStack():

    def __init__(self):
        self.stack = Stack()
        self.maxstack = Stack()
        self.top = self.stack.top

    def getMax(self , values):
        for element in values:
            self.stack.push(element)
            if self.stack.top.value and self.maxstack.top is None :
                self.maxstack.push(element)

            if (element > self.maxstack.top.value):
                self.maxstack.push(element)

        return self.maxstack.top.value



if __name__ == '__main__':

    print(MaxStack().getMax([3 , 1 , 5]))






