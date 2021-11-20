class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
# Recursive function to calculate the height of a given binary tree
def height(root):
    # base case: empty tree has a height of 0
    if root is None:
        return 0
    # recur for the left and right subtree and consider maximum depth
    return 1 + max(height(root.left), height(root.right))

 
if __name__ == '__main__':
    root = Node(45)
    root.left = Node(13)
    root.right = Node(10)
    root.left.left = Node(18)
    root.left.right = Node(22)
    root.right.left = Node(19)
    root.right.right = Node(21)
    print('The height of the binary tree is', height(root))