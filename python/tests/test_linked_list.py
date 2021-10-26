# from test_data import linked
import pytest
from linked_list.linked_list import Node,  LinkedList




def test_node_has_int_data():
    # Arrange any data that you need to run your test
    expected = 1
    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = node.data
    # Assert
    assert actual == expected


def test_node_has_str_data():
    # Arrange any data that you need to run your test
    expected = "a"
    # Act on the subject of the test to produce some actual output
    node = Node("a")
    actual = node.data
    # Assert
    assert actual == expected


def test_node_is_a_Node():
    # Arrange any data that you need to run your test
    expected = "Node"
    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = type(node).__name__
    # Assert
    assert actual == expected


def test_node_without_value():
    with pytest.raises(TypeError):
        node = Node()


def test_new_linked_list_is_empty():
    # Arrange
    expected = None
    ll = LinkedList()
    # Act
    actual = ll.head
    # Assert
    assert actual == expected


def test_linked_list_insert():
    # Arrange
    expected = 1
    ll = LinkedList()
    # Act
    ll.insert(1)
    # node = ll.head
    actual = ll.head.data
    # Assert
    assert actual == expected


def test_linked_list_insert_twice():
    # Arrange
    expected = 0
    ll = LinkedList()
    # Act
    ll.insert(6)
    ll.insert(0)
    node = ll.head
    actual = node.data
    # Assert
    assert actual == expected
    assert ll.head.nxt.data == 6


def test_linked_inclue():
    # Arrange
    expected = True
    ll = LinkedList()
    # Act
    ll.insert(1)
    ll.insert(3)
    actual = ll.includes(3)
    # Assert
    assert actual == expected
    assert ll.includes(1) == True
    assert ll.includes(4) == False


def test_linked_to_string():
    # Arrange
    expected = "{ a } -> { b } -> { c } -> NULL"
    ll = LinkedList()
    # Act
    ll.insert("c")
    ll.insert("b")
    ll.insert("a")
    # Assert
    actual = ll.to_string()
    # Assert
    assert actual == expected

def test_list_append():
   # Arrange
    expected = "{ a } -> { b } -> { c } -> { d } -> NULL"
    ll = LinkedList()
    # Act
    ll.insert("c")
    ll.insert("b")
    ll.insert("a")
    ll.append("d")
     # Assert
    actual = ll.to_string()
    # Assert
    assert actual == expected

def test_list_before():
       # Arrange
    expected = "{ d } -> { a } -> { b } -> { c } -> NULL"
    ll = LinkedList()
    # Act
    ll.insert("c")
    ll.insert("b")
    ll.insert("a")
    ll.insert_before("a", "d")
     # Assert
    actual = ll.to_string()
    # Assert
    assert actual == expected

def test_list_after():
       # Arrange
    expected = "{ a } -> { d } -> { b } -> { c } -> NULL"
    ll = LinkedList()
    # Act
    ll.insert("c")
    ll.insert("b")
    ll.insert("a")
    ll.insert_after("a", "d")
     # Assert
    actual = ll.to_string()
    # Assert
    assert actual == expected

def test_get_k_th():
    # Arrange
    expected = 3
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.kthFromEnd(2)
    print(actual)
    # Assert
    assert actual == expected

def test_get_k_th_if_number_passed_greater_than_length_of_list():
    # Arrange
    expected = "You are not allowed to enter a number is greater than length of list"
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.kthFromEnd(5)
    print(actual)
    # Assert
    assert actual == expected


def test_get_k_th_if_number_passed_is_negative():
    # Arrange
    expected = "You are not allowed to enter negative number"
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.kthFromEnd(-1)
    print(actual)
    # Assert
    assert actual == expected

def test_get_k_th_if_list_length_is_unity():
    # Arrange
    expected = 1
    # Actual
    ll = LinkedList()
    ll.append(1)
    actual = ll.kthFromEnd(0)
    print(actual)
    # Assert
    assert actual == expected
def test_get_k_th_if_list_in_the_middle():
    # Arrange

    expected = 3
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(4)
    ll.append(5)
    ll.insert_before(4, 3)
    actual = ll.kthFromEnd(2)

    # Assert
    assert actual == expected

def test_get_k_if_the_k_and_length_are_same():
    # Arrange
    # expected '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> None'
    expected = "The Length of array and the k you passed are same"
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(4)
    ll.append(5)
    ll.insert_before(4, 3)
    actual = ll.kthFromEnd(5)

    # Assert
    assert actual == expected
