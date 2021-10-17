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

    """Functio to insert a new node at the beginning """
    # def insert_before(self, value, new_value):

    #     for i in range((value)):
    #       new_node = Node(new_value)
    #       if value[i] == new_node:

    #            new_node.nxt = self.head
    #            self.head = new_node

    #            value.insert(i, new_node)

    def insert_before(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # def insert_after(self, value, new_value):

    #     if value is None:
    #         print ("The given previous node must inLinkedList.")
    #         return
    #     new_node = Node(new_value)

    #     new_node.nxt = value.nxt
    #     value.nxt = new_node

    def append(self, value):

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.nxt):
            last = last.nxt
        last.nxt =  new_node

aseel = LinkedList()
aseel.insert(2)
aseel.insert(1)
aseel.insert(6)
aseel.insert_before
# aseel.append(7)
print(aseel.to_string())
# print("for 2", aseel.includes(2))
# print("for 6", aseel.includes(6))
# print("for 3", aseel.includes(3))
