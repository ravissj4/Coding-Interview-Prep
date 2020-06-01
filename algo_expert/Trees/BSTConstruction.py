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
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else: # if the value == self.value
            return True

    def remove(self, value, parent = None):
        if value < self.value:
            if self.left != None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right != None:
                self.right.remove(value, self)
        else:
            # means value = self.value
            # if self node is not the self of the tree
                # case 1 : self has both left and right child
                # case 2 : self has only one child = left
                # case 3 : self has only one child = right
                # case 4 : self has no child      
            # else
                # self = None (happens when parent == None)
			# CASE 1 : both left and right children exist
			if self.left != None and self.right != None:
                inorderSuccessor = self.right.getMinValue()
                self.value = inorderSuccessor 
                self.right.remove(inorderSuccessor, self.right)
			elif parent == None:
                # means node to be deleted == self and
                # it either has only left or only right child
                # in either case, we need to make everything of 
                # self node == that node
                if self.left != None:
                    self.value = self.left.value
                    self.left = self.left.left
                    self.right = self.left.right
                elif self.right != None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    # this self node does not have any children, do nothing !
					pass
            else: 
				# case : parent != None and left child exists
				
                if parent.left == self:
                    # if self.left != None:
                    #     parent.left = self.left
                    # else:
                    #     parent.left = self.right
                    parent.left = self.left if self.left != None else self.right
                elif parent.right == self:
                    parent.right = self.left if self.left != None else self.right

                    
        return self
    
    def getMinValue(self):
        while self.left is not None:
            self = self.left
        return self
