from node import Node

class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # Symmetric Order in Tree Traversal
    def in_order(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.in_order(node.left)
        print(node, end='')
        if node.right:
            self.in_order(node.right)
            print(')', end='')

    def post_order_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.post_order_traversal(node.left)
        if node.right:
            self.post_order_traversal(node.right)
        print(node, end="")

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright+1
        return hleft+1

# in order test
tree = BinaryTree()
n1 = Node('a')
n2 = Node('+')
n3 = Node('*')
n4 = Node('b')
n5 = Node('-')
n6 = Node('/')
n7 = Node('c')
n8 = Node('d')
n9 = Node('e')

n6.left = n7
n6.right = n8
n5.left = n6
n5.right = n9
n3.left = n4
n3.right = n5
n2.left = n1
n2.right = n3
tree.root = n2 # change root to see another height

tree.in_order()

print("")
print(f"Height: {tree.height()}")


# post order test
n1 = Node('f')
n2 = Node('r')
n3 = Node('i')
n4 = Node('e')
n5 = Node('n')
n6 = Node('d')
n7 = Node('s')
n8 = Node('h')
n9 = Node('i')
n0 = Node('p')

n0.left = n6
n0.right = n9
n6.left = n1
n6.right = n5
n5.left = n2
n5.right = n4
n4.right = n3
n9.left = n8
n8.right = n7
tree.root = n0 # change root to see another height

tree.post_order_traversal()

print("")
print(f"Height: {tree.height()}")