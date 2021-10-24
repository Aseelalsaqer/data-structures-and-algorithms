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


def test_linked_list_append():
    # Arrange
    expected = "{ a } -> { b } -> { c } -> { A } -> NULL"
    ll = LinkedList()
    # Act
    ll.insert("c")
    ll.insert("b")
    ll.insert("a")
    ll.append("A")
    actual = ll.to_string()
    # Assert
    assert actual == expected


def test_append_multie_nodes():
    # Arrange
    expected = "{ 1 } -> { 5 } -> { 6 } -> NULL"
    # Act
    ll = LinkedList()
    # Assert
    node1 = ll.insert(1)
    node2 = ll.append(5)
    node3 = ll.append(6)
    actual = ll.to_string()
    # Assert
    assert actual == expected


def test_insert_before_first_node():
    # Arrange
    expected = "{ 3 } -> { 5 } -> { 1 } -> NULL"
    # Act
    ll = LinkedList()
    # Assert
    node1 = ll.insert(1)
    node1 = ll.insert(3)
    node2 = ll.insert_before(5, 1)
    actual = ll.to_string()
    # Assert
    assert actual == expected


def test_insert_before_middle_node():
    # Arrange
    expected = "{ 5 } -> { 1 } -> { 3 } -> NULL"
    # Act
    ll = LinkedList()
    # Assert
    node1 = ll.insert(1)
    node1 = ll.insert(3)
    node2 = ll.insert_before(5, 3)
    actual = ll.to_string()
    # Assert
    assert actual == expected


def test_insert_before_empty_list():
    # Arrange
    expected = "Empty linked list"
    # Act
    ll = LinkedList()
    # Assert

    node2 = ll.insert_before(5, 1)
    actual = ll.to_string()
    # Assert
    assert actual == expected


def test_insert_after_list_tile():
    # Arrange
    expected = "This the linked list tile"
    # Act
    ll = LinkedList()
    # Assert
    node1 = ll.insert(5)
    node2 = ll.insert(4)
    actual = ll.insert_after(5, 4)
    # Assert
    assert actual == expected


def test_insert_after_middle_node():
    # Arrange
    expected = "{ 5 } -> { 3 } -> { 1 } -> NULL"
    # Act
    ll = LinkedList()
    # Assert
    node1 = ll.insert(1)
    node1 = ll.insert(3)
    node2 = ll.insert_after(5, 3)
    actual = ll.to_string()
    # Assert
    assert actual == expected


def test_insert_after():
    # Arrange
    expected = "{ 5 } -> { 1 } -> { 3 } -> NULL"
    # Act
    ll = LinkedList()
    # Assert
    node1 = ll.insert(5)
    node2 = ll.insert(1)
    actual = ll.insert_after(3, 1)
    # Assert
    assert actual == expected
