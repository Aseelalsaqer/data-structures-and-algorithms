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
        count = 1
        while pointer.nxt:
            count += 1
            pointer = pointer.nxt
        pointer = self.head

        if k >= count:
            return "You are not allowed to enter a number greater than length of the list"
        elif k < 0:
            return "You are not allowed to enter negative number"
        value = count-k-1
        for i in range(count):

            if i == value:

                return pointer.data


            pointer = pointer.nxt

    def zip_lists(list1, list2):
        """function takes two lists as argument and return one list which is result of alternate between the two lists and return a reference to the head of the zipped list."""

        first = list1.head
        second = list2.head

        if not first and not second:

            return 'There is no lists to zip'


        fixed_node = ""

        while first and second:
            if second:
                fixed_node = first.nxt
                first.nxt = second
                first = fixed_node

            if first:
                fixed_node = second.nxt
                second.nxt = first
                second = fixed_node

        return str(list1)





# aseel = LinkedList()
# aseel.insert(2)
# aseel.insert(1)
# aseel.insert(6)
# print(aseel.to_string())

aseel = LinkedList()
aseel.insert(2)
aseel.insert(1)
aseel.insert(6)
aseel.insert(8)
aseel.insert(3)
# aseel.insert_before(3 , 10)
# aseel.append(7)
# print(aseel.kthFromEnd(1))

print(aseel.to_string())

# print("for 2", aseel.includes(2))
# print("for 6", aseel.includes(6))
# print("for 3", aseel.includes(3))
