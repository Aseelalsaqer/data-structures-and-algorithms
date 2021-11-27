from code_challenges.hashtable.hash import HashTable

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class binarytree:
    def __init__(self):
        self.root = None


    def pre_order(self):
            self.values = []
            if self.root == None:
                return "empty tree"
            def ordering(node):
                self.values += [node.value]
                if node.left:
                    ordering(node.left)
                if node.right:
                    ordering(node.right)
                return self.values
            return ordering(self.root)




def hash_intersection(bt1, bt2):
    matches = []
    binary_tree1 = bt1.pre_order()
    binary_tree2 = bt2.pre_order()
    hashtable = HashTable()

    for value in binary_tree1:
        hashtable.add(key=str(value), value=value)
    for value in binary_tree2:
        if hashtable.contains(str(value)):
            matches.append(value)
    return matches


