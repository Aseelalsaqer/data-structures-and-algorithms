class Node:
    """
    A class representing a Node
    Attributes
    ----------
    Methods
    -------
    __init__(data, nxt_):
        the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the nxt_
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


    def insert_after(self, value, new_value):
        """
         function will add a new value as a node after the given value

         """
        node = Node(new_value)
        current_value_node = self.head
        if current_value_node.data == value:
            node.nxt = self.head
            self.head = node
        else:
            while current_value_node.nxt:
                if current_value_node.nxt.data == value:
                    node.nxt = current_value_node.nxt
                    current_value_node.nxt = node
                    break
                current_value_node = current_value_node.nxt

    def insert_before(self, value, new_value):
        """
         function will add a new node before the given value

         """
        new_node = Node(new_value)
        current_value = self.head
        while current_value:
            if current_value.data == value:
                new_node.nxt = current_value.nxt
                current_value.nxt = new_node
                break
            current_value = current_value.nxt


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
        while (pointer.nxt):
            if (count == k):
                return pointer.data
            count += 1
            pointer = pointer.nxt

        if k > count:
            return "You are not allowed to enter a number is greater than length of list"
        elif k < 0:
            return "You are not allowed to enter negative number"



aseel = LinkedList()
aseel.insert(2)
# print(aseel.to_string())
aseel.insert(1)
# print(aseel.to_string())
aseel.insert(6)
aseel.insert(8)
aseel.insert(3)


print(aseel.kthFromEnd(4))
print(aseel.to_string())
# print(aseel.to_string())
# aseel.insert_before(1, 3)
# aseel.append(7)
# aseel.insert_after(1, 7)

# print(aseel.to_string())
# print("for 2", aseel.includes(2))
# print("for 6", aseel.includes(6))
# print("for 3", aseel.includes(3))
