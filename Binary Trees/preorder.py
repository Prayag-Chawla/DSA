
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
           
def treeInput():
        
    rootData = int(input())
    if rootData == -1:
        return None
    
    root = BinaryTreeNode(rootData)
    root.left = treeInput()
    root.right = treeInput()

    return root

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, end = ":")
    
    if root.left is not None:
        print("L", root.left.data, end = ",")
        
    if root.right is not None:
        print("R", root.right.data, end = " ")
        
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def preOrder(root):
    if root == None:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)

root = treeInput()
preOrder(root)

print("Detailed Tree ")

printTreeDetailed(root)   