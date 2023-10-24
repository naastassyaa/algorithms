class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    visited = []

    def traverse_in_order(node):
        if node.left:
            traverse_in_order(node.left)
        visited.append(node)
        if node.right:
            traverse_in_order(node.right)

    traverse_in_order(tree)
    pos = visited.index(node)
    for i in visited[pos:]:
        if i.value > node.value:
            return i


root = BinaryTree(10)
root.left = BinaryTree(5)
root.right = BinaryTree(15)
root.left.left = BinaryTree(3)
root.left.right = BinaryTree(7)
root.right.right = BinaryTree(20)
root.right.right.left = BinaryTree(12)

node_to_find_successor = root.left
successor = find_successor(root, node_to_find_successor)

if successor:
    print(successor.value)
else:
    print("Немає наступника для даної вершини.")
