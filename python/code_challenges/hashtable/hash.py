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
        self.array = [None] * size

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

        if not self.array[index]:
          self.array[index] = LinkedList()
        my_value = [key,value]
        self.array[index].insert(my_value)
        return self.array[index]

    def get(self, key):
      """
      Retrieve the most recent value of in oour hasmap for the given key

      :param key str
      :rvalue any
      """

      index = self.__hash(key)

      if self.array[index]:

        linked_list = self.array[index]
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
        if self.array[index] is None:
            return False

        current = self.array[index].head
        while (current):
            key_inside = current.value[0]
            if key_inside == key:
                return True
            current = current.next
        return False
# ht = HashTable()
# ht.add('aseel', 10)
# ht.add('asel', 12)
# ht.add('asl', 18)

# print(ht.get('asl'))

# print(ht.contains('aseel'))
def left_join(ht1, ht2):
    result = []
    for i in ht1.array:
        if i:
            lj = []
            current_value = i.head
            while current_value:
                lj.append(current_value.value[0])
                lj.append(current_value.value[1])
                if ht2.contains(current_value.value[0]):
                    lj.append(ht2.get(current_value.value[0]))
                else:
                    lj.append(None)
                current_value = current_value.next

            result.append(lj)
    return result


def checkString(str):
    ht1 = HashTable()

    for char in str:
        if ht1.contains(char):
            return False;
        else :
            ht1.add(char, char);
    return True;


str = "I love cats"
print(checkString(str.replace(" ", "")))


# ht1 = HashTable()
# ht1.add("aseel", 10)
# ht1.add("asel", 12)
# ht1.add("asl", 18)


# ht2 = HashTable()
# ht2.add("aseel", 20)
# ht2.add("asxl", 12)
# ht2.add("asl", 16)

# actual = left_join(ht1, ht2)
# print(actual)

