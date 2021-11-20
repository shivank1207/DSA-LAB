# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
# Function to return the total number of nodes in a given binary tree
def size(root):
    return 1 + size(root.left) + size(root.right) if root else 0
 
# Returns true if the size of the given binary tree or any of its subtrees is exactly `n/2`
def checkSize(root, n):
    if root is None:
        return False
    if 2 * size(root) == n:
        return True
    return checkSize(root.left, n) or checkSize(root.right, n)
  
# Function to check if a given binary tree can be split into
# two binary trees of equal size
def splitTree(root):
    # count the total number of nodes in the binary tree
    n = size(root)
    # a binary tree can be evenly split only if it has an even number of nodes
    return (n % 2 == 0) and checkSize(root, n)
 
 
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.right = Node(60)
    if splitTree(root):
        print('The binary tree can be split')
    else:
        print('The binary tree cannot be split')