"""
The implementation of Node class, Linked list class, and Hashmap class.
"""


class Node:
    def __init__(self, value=None, next_=None):
        """
      Initalization the Node
      """
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        """
        The constructor method for the linked list. Initializes the head of a linked list to None.
        """
        self.head = None

    def insert(self, value):
        """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """
        self.head = Node(value, self.head)


class HashTable:
    def __init__(self, size=1024):
        """
        Initalization of Hash table

        """
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value pari in a Node at that index.
        """
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        """
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.

        Arg: Takes the key and value
        Return : No return value
        """

        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()
        my_value = [key,value]
        self.__buckets[index].insert(my_value)

    def get(self, key):
      """
      Retrieve the most recent value of in oour hasmap for the given key

      :param key str
      :rvalue any
      """

      index = self.__hash(key)

      if self.__buckets[index]:

        linked_list = self.__buckets[index]
        current = linked_list.head
        while current:

          if current.value[0] == key:

            return current.value[1]
          current = current.next


      return None


    def contains(self, key):
        """
        A method for chicking if the value exist or not.

        Arg: Takes the key and value
        Return : True , False
        """
        index = self.__hash(key)
        if self.__buckets[index] is None:
            return False

        current = self.__buckets[index].head
        while (current):
            key_inside = current.value[0]
            if key_inside == key:
                return True
            current = current.next
        return False
ht = HashTable()
ht.add('aseel', 10)
ht.add('asel', 12)
ht.add('asl', 18)

print(ht.get('asl'))

print(ht.contains('aseel'))
