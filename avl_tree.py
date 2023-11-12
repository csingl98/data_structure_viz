class AVLNode():
    def __init__(self, value) -> None:
        self.value = value
        self.height = 0
        self.leftChild = None
        self.rightChild = None


class AVLTree():
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value):
        self.root = self.insert_node(self.root, value)
        return
        
    def insert_node(self, root, value):
        if root == None:
            return AVLNode(value)

        if value > root.value:
            root.rightChild = self.insert_node(root.rightChild, value)

        else:
            root.leftChild = self.insert_node(root.leftChild, value)
        
        root.height = self.setHeight(root)

        return self.balance(root)

    def balance(self, root):

        if self.isLeftHeavy(root):
            if self.balanceFactor(root.leftChild) < 0:
                root.leftChild = self.rotateLeft(root.leftChild)

            return self.rotateRight(root)
        
        elif self.isRightHeavy(root) :
            if self.balanceFactor(root.rightChild) > 0:
                root.rightChild = self.rotateRight(root.rightChild)
            
            return self.rotateLeft(root)

        return root

    
    def rotateRight(self, root):
        new_root = root.leftChild

        root.leftChild = new_root.rightChild
        new_root.rightChild = root

        new_root.height = self.setHeight(new_root)
        root.height = self.setHeight(root)

        return new_root

    def rotateLeft(self, root):
        new_root = root.rightChild

        root.rightChild = new_root.leftChild
        new_root.leftChild = root

        new_root.height = self.setHeight(new_root)
        root.height = self.setHeight(root)

        return new_root

    
    def setHeight(self, root):
        return max(self.height(root.leftChild), self.height(root.rightChild)) + 1

    def height(self, node):       
        return -1 if node == None else node.height

    def isLeftHeavy(self, node):
        return self.balanceFactor(node) > 1

    def isRightHeavy(self, node):
        return self.balanceFactor(node) < -1

    def balanceFactor(self, node):
        return 0 if node == None else self.height(node.leftChild) - self.height(node.rightChild)


    def isBalanced(self):
        self.checkBalance(self.root)

    def checkBalance(self, node):
        if node == None:
            return

        if self.isLeftHeavy(node) or self.isRightHeavy(node):
            return False

        self.checkBalance(node.leftChild)
        self.checkBalance(node.rightChild)

        return True

    def isPerfect(self):
        pass


def main():
    tree = AVLTree()
    tree.insert(10)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)



if __name__ == "__main__":

    main()

