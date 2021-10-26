class Node:
    """
    A class representing a Node
    Attributes
    ----------
    Methods
    -------
    __init__(data, next_):
        the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the next_
    """

    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt



class LinkedList:
    """
    A class for creating instances of a Linked List.
    Data and other attributes defined here:
    head: Node | None
    Methods defined here
    insert(value: any)
    contains(value: any) -> bool
    """

    def __init__(self):
        self.head = None



    def insert(self, value):
        """"
        Insert creates a Node with the value that was passed and adds
        it to the head of the linked list shifting all other values down
        arguments:
        value : any
        returns: None
        """

        self.head = Node(value, self.head)

    def includes(self, value):
        """insert function will loop through all the inside the dictionary(object)
                Arrgument
                Value:any
                returns :True/False"""
        element = self.head
        while element:
            if element.data == value:
                return True
            elif element.nxt is not None:
                element = element.nxt
            else:
                return False

    def to_string(self):
        """to_string function will loop trough all the dictionary (object)
                Arrgument :no arrgument
                return all the data inside the dictionary"""
        string = ""
        element = self.head
        while element:
            string += "{ "+str(element.data)+" } -> "
            element = element.nxt
        string += "NULL"
        return string



    def insert_before(self ,newValue,valueToAddBefore):
        """
        adding new node with  new value  before the node that has the value specified

        """

        current =self.head
        if not current:
            return "NULL"
        while current.nxt:
            if current.nxt.data == valueToAddBefore:
                new_node =Node(newValue)
                new_node.nxt = current.nxt
                current.nxt=new_node
        current=current.nxt

    def insert_after(self ,newValue,valueToAddafter):
        """
        adding new node with  new value  after the node that has the value specified

        """

        current =self.head
        if not current.nxt:
            return "This the linked list tile"
        while current.nxt:
            if current.data == valueToAddafter:
                new_node =Node(newValue)
                new_node.nxt = current.nxt
                current.nxt=new_node
        current=current.nxt

    def append(self, value):

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.nxt):
            last = last.nxt
        last.nxt =  new_node

    def kthFromEnd(self, k):
        """
        this function return the kth value of list

        """
        pointer = self.head
        count = 0
        while (pointer):
            if (count == k):
                return pointer.data
            count += 1
            pointer = pointer.nxt
        if k == count:
            return "The Length = k you passed are same"
        elif k > count:
            return "You are not allowed to enter a number greater than length of the list"
        elif k < 0:
            return "You are not allowed to enter negative number"
        else:
            return 0

# aseel = LinkedList()
# aseel.insert(2)
# aseel.insert(1)
# aseel.insert(6)
# print(aseel.to_string())

aseel = LinkedList()
aseel.insert(2)
aseel.insert(1)
aseel.insert(6)
# aseel.insert_before(3 , 10)
# aseel.append(7)
aseel.kthFromEnd(2)
print(aseel.to_string())

# print("for 2", aseel.includes(2))
# print("for 6", aseel.includes(6))
# print("for 3", aseel.includes(3))
