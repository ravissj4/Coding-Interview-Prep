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


def minHeightBst(array):
    return constructMinHeightBST(array, None)

def constructMinHeightBST(array, bst):
	# print(f'array = {array}, len = {len(array)}')
    if len(array) == 0:
        return
    mid = (len(array) - 1) // 2
    
    valueToAdd = array[mid]
	# print(f"value to add = {valueToAdd}")
    if bst == None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
    
    constructMinHeightBST(array[:mid], bst)
    constructMinHeightBST(array[mid+1:], bst)

    return bst
