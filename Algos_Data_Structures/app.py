from node import Node
from binary_tree import BinaryTree

# numbers = [13, 56, 38, 44, 54, 22, 1, 7, 9, 34, 717, 6756, 59, 3, 4, 53, 5, 98, 95, 14, 918845]


tree = BinaryTree(Node(6))

nodes = [5, 3, 9, 7, 8, 7.5, 12, 11]

for n in nodes:
    tree.add(Node(n))


tree.inorder()
tree.delete(9)
print()
tree.inorder()
