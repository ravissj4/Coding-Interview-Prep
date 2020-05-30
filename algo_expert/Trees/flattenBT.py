# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    # Write your code here.
    leftmostNode, rightmostNode = flattenBT(root)
	return leftmostNode.value

def flattenBT(node):
    if node.left is None:
        greatestNodeLST = node
    else:
        greatestLeft, smallestRight = flattenBT(node.left)
        connect_nodes(greatestLeft, node)
        greatestNodeLST = greatestLeft
    if node.left is None:
        smallestNodeRST = node
    else:
        greatestLeft, smallestRight = flattenBT(node.right)
        connect_nodes(node, smallestRight)
        smallestNodeRST = smallestRight
        
    return [greatestNodeLST, smallestNodeRST]

def connect_nodes(left, right):
    left.right = right
    right.left = left