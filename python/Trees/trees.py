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

    def max_value(self):
        if self.root:
            return self.maxvalue(self.root)

    def maxvalue(self ,node):
        if node.right:
            return self.maxvalue(node.right)
        return node.value



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

   aseel.add(15)
   aseel.add(14)
   aseel.add(16)
   aseel.add(13)
   aseel.add(17)

#    aseel.add(3)
# print(aseel.inorder())
# print(aseel.postorder())
# print(aseel.preorder())
# print(aseel.Contains(6))
# print(aseel.Contains(7))
print(aseel.max_value())
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
# print(breadth_first(aseel))


def fizz_buzz_tree(tree):
    new_tree = []
    if tree.root == None :
          return "empty tree"
    else :

            def ordering(root):
                if root.value%3 == 0 and root.value%5 ==0:
                        new_tree.append("FizzBuzz")
                elif root.value%3 == 0 :
                        new_tree.append("Fizz")
                elif root.value%5 == 0:
                        new_tree.append("Buzz")
                else :
                    new_tree.append(str(root.value))

                if root.left:
                    ordering(root.left)
                if root.right:
                    ordering(root.right)
            ordering(tree.root)
            return new_tree
# x = fizz_buzz_tree(aseel)
# print(x)


def odd_sum(tree):
    odd_num = []
    if tree.root == None :
        return "empty tree"
    def ordering(root):
        if root.value%2 !=0 :
            odd_num.append(root.value)

        if root.left :
            ordering(root.left)
        if root.right:
            ordering(root.right)
    ordering(tree.root)
    return sum(odd_num)
# oddsum = odd_sum(aseel)
# print(oddsum)
