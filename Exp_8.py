def printIncreasing(keys, low, high):
    if low > high:
        return
    # recur for the left subtree
    printIncreasing(keys, low*2 + 1, high)
    # print the root node
    print(keys[low], end=' ')
    # recur for the right subtree
    printIncreasing(keys, low*2 + 2, high)
 
 
if __name__ == '__main__':
    keys = [20, 15, 25, 13, 17, 23, 30]
    printIncreasing(keys, 0, len(keys) - 1)