class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # < Go left
        # >= Go right
        if value is None:
            return None
            
        if value < self.value:

            if self.left is None:
                self.left = BinarySearchTree(value)

            else:
                 self.left.insert(value)

        if value >= self.value:

            if self.right is None:
                self.right = BinarySearchTree(value)

            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the key is present at root, we return root. If key is greater than root's key, 
        # we recur for right subtree of root node. Otherwise we recur for left subtree.
        if target is None:
            return False

        if target == self.value:
            return True

        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)


        
