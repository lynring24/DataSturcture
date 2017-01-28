class BinaryTree():
    def __init__(self,root):
        self.left = None
        self.right = None
        self.root = root

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNodeValue(self,value):
        return self.root

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.right
            self.left = tree

def printTree(tree):
    if tree != None:
        printTree(tree.getLeftChild)
        print(tree.getNodeValue())
        printTree(tree.getRightChild)
