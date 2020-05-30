# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        tree = self
        if value < tree.value:
            if tree.left is None:
                tree.left = BST(value)
            else:
                tree.left.insert(value)
        else:
            if tree.right is None:
                tree.right = BST(value)
            else:
                tree.right.insert(value)
        return self

    def contains(self, value):
        # Write your code here.
        tree = self
        if value < tree.value:
            if tree.left is None:
                return False
            else:
                return tree.left.contains(value)
        elif value > tree.value:
            if tree.right is None:
                return False
            else:
                return tree.right.contains(value)
        else:
            return True

    def remove(self, value, parent = None):
        # Write your code here.
        # Do not edit the return statement of this method.
        root = self
        if value < root.left:
            if root.left is None:
                return -1
            else:
                root.left.remove(value, root)
        elif value > root.right:
            if root.right is None:
                return -1
            else:
                root.right.remove(value, root)
        else:
            # means value = root.value
            # if root node is not the root of the tree
                # case 1 : root has both left and right child
                # case 2 : root has only one child = left
                # case 3 : root has only one child = right
                # case 4 : root has no child      
            # else
                # root = None

            if parent is None:
                root = None
            else:
                if root.left is not None and root.right is not None:
                    inorderSuccessor = root.right.getMinValue()
                    root.value = inorderSuccessor 
                    root.right.remove(inorderSuccessor, root.right)
                elif root.left is None:
                    if parent.left == root:
                        parent.left = root.right
                    else:
                        parent.right = root.right
                elif root.right is None:
                    if parent.left == root:
                        parent.left = root.left
                    else:
                        parent.right = root.left
                elif root.left is None and root.right is None:
                    if parent.left == root:
                        parent.left = None
                    else:
                        parent.right = None
        return self
    
    def getMinValue(self):
        while self.left is not None:
            self = self.left
        return self
