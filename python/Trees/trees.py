class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class binarytree:

    def __init__(self):
        self.root = None
    def inorder(self):
            self.values = []
            if not self.root:
                return "empty tree"
            def ordering(node):
                if node.left:
                    ordering(node.left)
                self.values += [node.value]
                if node.right:
                    ordering(node.right)
                return self.values
            return ordering(self.root)

    def preorder(self):
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

    def postorder(self):
            self.values = []
            if not self.root:
                return "empty tree"
            def ordering(node):
                if node.left:
                    ordering(node.left)
                if node.right:
                    ordering(node.right)
                self.values += [node.value]
                return self.values
            return ordering(self.root)
    def max_value(self):
          self.values = []
          if self.root == None:
                return "empty tree"
          def ordering(node):
                self.values += [node.value]
                if node.left:
                    ordering(node.left)
                if node.right:
                    ordering(node.right)
                return max(self.values)
          return ordering(self.root)



class binarysearchtree(binarytree):

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root
            while current:
                if value < current.value:
                    if current.left == None:
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if current.right == None:
                        current.right = Node(value)
                        break
                    current = current.right

    def Contains(self, value):
        if self.root == None:
            return 'empty tree'
        else:
            current = self.root
            while current:
                if current.value == value:
                    return "the value is exist"
                elif value < current.value:
                    if current.left == None:
                        return "dose not exist"
                    current = current.left
                else:
                    if current.right == None:
                        return "dose not exist"
                    current = current.right


aseel= binarysearchtree()
if __name__ == '__main__':

   aseel.add(1)
   aseel.add(2)
   aseel.add(7)
   aseel.add(11)
   aseel.add(3)
# print(aseel.inorder())
# print(aseel.postorder())
# print(aseel.preorder())
# print(aseel.Contains(6))
# print(aseel.Contains(7))
# print(aseel.max_value())
def breadth_first(tree):
    list=[]
    if tree.root==None:
        return "empty tree"
    else:
        list.append(tree.root.value)
        def ordering(tree):
            if tree.left:
                list.append(tree.left.value)
            if tree.right:
                list.append(tree.right.value)
            if tree.left:
                ordering(tree.left)
            if tree.right:
                ordering(tree.right)
        ordering(tree.root)
        return list
print(breadth_first(aseel))


