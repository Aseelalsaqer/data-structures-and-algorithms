from linked_list.linked_list import Node,  LinkedList
import pytest


# def test_version():
#     assert __version__ == '0.1.0'


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


def test_append():
    linked_list = LinkedList()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.append(74)
    linked_list.to_string()
    # actual = str(ll)
    # expected = '{10} -> {6} -> {3} -> {74} -> NULL'
    # assert actual == expected
    assert linked_list.to_string() == "{4} -> {7} -> {74} -> Null"

def test_multiple_append():
    linked_list = LinkedList()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.append(74)
    linked_list.append(66)
    linked_list.to_string()
    assert linked_list.to_string() == "{4} -> {7} -> {74} -> {66} -> Null"


def test_insert_before_middle():
    linked_list = LinkedList()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.insert(1)
    linked_list.append(74)
    linked_list.append(66)
    linked_list.insert_before(7,'before middle')
    linked_list.to_string()
    assert linked_list.to_string() == "{1} -> {4} -> {'before middle'} -> {7} -> {74} -> {66} -> Null"

def test_insert_before_first():
    linked_list = LinkedList()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.insert(1)
    linked_list.append(74)
    linked_list.append(66)
    linked_list.insert_before(1,100)
    linked_list.to_string()
    assert linked_list.to_string() == "{100} -> {1} -> {4} -> {7} -> {74} -> {66} -> Null"


def test_insert_after_middle():
    linked_list = LinkedList()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.insert(1)
    linked_list.append(74)
    linked_list.append(66)
    linked_list.insert_after(7,'after middle')
    linked_list.to_string()
    assert linked_list.to_string() == "{1} -> {4} -> {7} -> {'after middle'} -> {74} -> {66} -> Null"


def test_insert_after_end():
    linked_list = LinkedList()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.insert(1)
    linked_list.append(74)
    linked_list.append(66)
    linked_list.insert_after(66,'after end')
    linked_list.to_string()
    assert linked_list.to_string() == "{1} -> {4} -> {7} -> {74} -> {66} -> {'after end'} -> Null"
