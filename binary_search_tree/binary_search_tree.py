import sys
sys.path.append('../queue_and_stack')
 


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = self

        while node:
            if value < node.value:
                if node.left is None:
                    node.left = BinarySearchTree(value)
                    return 
                else: 
                    node = node.left
            else:
                if node.right is None:
                    node.right = BinarySearchTree(value)
                    return
                else: 
                    node = node.right
             

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        node = self
        
        while node:
            if node.value == target:
                return True

            if target > node.value:
                node = node.right
            elif target < node.value:
                node = node.left 
    
        return False
    # Return the maximum value found in the tree
    def get_max(self):
    
        node = self
         
        while node:
            if not node.right:
                return node.value
            node = node.right

        return 0

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
