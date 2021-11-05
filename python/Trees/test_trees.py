from trees import __version__

from Trees.trees import  binarysearchtree



# def test_version():
#     assert __version__ == '0.1.0'



# first test "successfully instantiate an empty tree"
def test_empty_tree():
    tree = binarysearchtree()
    actual = tree.root
    expected = None
    assert actual == expected

# second test "successfully instantiate a tree with a single root node"
def test_single_root_node():
    aseel = binarysearchtree()
    aseel.add(1)
    aseel.add(2)
    aseel.add(3)
    aseel.add(4)
    actual = aseel.root.value
    expected = 1
    assert actual == expected

# third test "successfully add a left child and right child to a single root node"
def test_left_and_right_single_root_node():
    aseel = binarysearchtree()
    aseel.add(10)
    aseel.add(2)
    aseel.add(30)
    actual = (aseel.root.left.value, aseel.root.right.value)
    expected = (2,30)
    assert actual == expected

# fourth test "successfully return a collection from an inorder traversal"
def test_inorder_traversal():
    aseel = binarysearchtree()
    aseel.add(1)
    aseel.add(5)
    aseel.add(2)
    aseel.add(7)
    aseel.add(11)
    aseel.add(3)
    actual = aseel.inorder()
    expected = [1, 2, 3, 5, 7, 11]
    assert actual == expected

# fifth test "successfully return a collection from a preorder traversal"
def test_preorder_traversal():
    aseel = binarysearchtree()
    aseel.add(1)
    aseel.add(5)
    aseel.add(2)
    aseel.add(7)
    aseel.add(11)
    aseel.add(3)
    actual = aseel.preorder()
    expected = [1, 5, 2, 3, 7, 11]
    assert actual == expected

# sixth test "successfully return a collection from a postorder traversal"
def test_postorder_traversal():
    aseel = binarysearchtree()
    aseel.add(1)
    aseel.add(5)
    aseel.add(2)
    aseel.add(7)
    aseel.add(11)
    aseel.add(3)
    actual = aseel.postorder()
    expected = [3, 2, 11, 7, 5, 1]
    assert actual == expected

# extra test "successfully return the value "dose not exist" in the tree "
def test_value_dne():
    aseel = binarysearchtree()
    aseel.add(1)
    aseel.add(5)
    aseel.add(2)
    aseel.add(7)
    aseel.add(11)
    aseel.add(3)
    actual = aseel.Contains(4)
    expected = "dose not exist"
    assert actual == expected

# extra test "successfully return if the valeu exist in the tree "
def test_value_exist():
    aseel = binarysearchtree()
    aseel.add(1)
    aseel.add(5)
    aseel.add(2)
    aseel.add(7)
    aseel.add(11)
    aseel.add(3)
    actual = aseel.Contains(11)
    expected = "the value is exist"
    assert actual == expected
#   to return the max value of binary tree

def test_value_max_1():
    aseel = binarysearchtree()
    aseel.add(1)
    aseel.add(5)
    aseel.add(2)
    aseel.add(7)
    aseel.add(11)
    aseel.add(3)
    actual = aseel.max_value()
    expected = 11
    assert actual == expected

#   to return the max value of binary tree
def test_value_max_2():
    aseel = binarysearchtree()
    aseel.add(5)
    aseel.add(2)
    aseel.add(7)
    aseel.add(3)
    actual = aseel.max_value()
    expected = 7
    assert actual == expected



