import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root == None:
        return 0
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    
    return 1 + max(leftHeight, rightHeight)     
    

def buildLevelTree():
    
    root = BinaryTreeNode(int(input()))
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = int(input())
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = int(input())
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
root = buildLevelTree()
print(height(root))