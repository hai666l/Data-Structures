"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        currNode = self                                         # Start at top node
        while 1:                                                # Traverse infinitely until we return @ end of tree

            if value >= currNode.value:                         # Compare value w/ right
                if currNode.right:                              # Check if we reached end of tree
                    currNode = currNode.right                   # We didn't, traverse right, loop will run on new current ndoe
                else:
                    currNode.right = BSTNode(value)             # Add new leaf if found end of tree
                    return

            else:                                               # Same process if value <= left
                if currNode.left:
                    currNode = currNode.left
                else:
                    currNode.left = BSTNode(value)
                    return
                    

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        currNode = self
        while 1:
            if target > currNode.value:                 # Check if target is > current node value
                if currNode.right:                      
                    currNode = currNode.right           # Traverse right if .right exists
                else:
                    return False                        # Reached end of list, target not found

            elif target < currNode.value:               # Same process if target < current node value
                if currNode.left:
                    currNode = currNode.left
                else:
                    return False
            else:                                       # Target is equal to current node value, target found in list
                return True
            

    # Return the maximum value found in the tree
    def get_max(self):
        maxFound = self.value
        currNode = self
        while currNode.right:               # While tree has a .right, maxFound is equal to it's value
            currNode = currNode.right
            maxFound = currNode.value
        return maxFound

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
"""

bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()

"""