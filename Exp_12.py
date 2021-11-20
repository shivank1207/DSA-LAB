# A class to store a Trie node
class TrieNode:
    def __init__(self):
        # `count` and `key` is only set for leaf nodes
        # `key` stores the string, and `count` stores its frequency so far
        self.key = None
        self.count = 0
        # each node stores a dictionary to its child nodes
        self.character = {}
 
 
# Iterative function to insert a string into a Trie
def insert(head, s):
    # start from the root node
    curr = head
    for c in s:
        # go to the next node and create a new node if the path doesn't exist
        curr = curr.character.setdefault(c, TrieNode())
    # store key and its count in leaf nodes
    curr.key = s
    curr.count += 1
 
 
# Function to perform preorder traversal on a Trie and
# find a word with the maximum frequency
def preorder(curr, key='', max_count=0):
    # return false if Trie is empty
    if curr is None:
        return key, max_count
    for (k, v) in curr.character.items():
        # leaf node has a non-zero count
        if max_count < v.count:
            key = v.key
            max_count = v.count
        # recur for current node's children
        key, max_count = preorder(v, key, max_count)
    return key, max_count
 
 
if __name__ == '__main__':
    words = [
        'code', 'coder', 'coding', 'codable', 'codec', 'codecs', 'coded',
        'codeless', 'codec', 'codecs', 'codependence', 'codex', 'codify',
        'codependents', 'codes', 'code', 'coder', 'codesign', 'codec',
        'codeveloper', 'codrive', 'codec', 'codecs', 'codiscovered'
    ]
    # Insert all keys into a Trie
    head = TrieNode()
    for word in words:
        insert(head, word)
    # perform preorder traversal on a Trie and find the key with a maximum frequency
    key, count = preorder(head)
    print('Word :', key)
    print('Count:', count)