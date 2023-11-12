import math


class Node():

    def __init__(self, value) -> None:
        self.value = value
        self.leftChild = None
        self.rightChild = None

class Tree():

    def __init__(self) -> None:
        self.root = None

    
    def insert(self, value):

        insert_node = Node(value)

        if self.root == None:
            self.root = insert_node
            return

        current_node = self.root
        previous_node = None

        while True:

            if insert_node.value > current_node.value:
                if current_node.rightChild == None:
                    current_node.rightChild = insert_node
                    break
                current_node = current_node.rightChild

            else:
                if current_node.leftChild == None:
                    current_node.leftChild = insert_node
                    break
                current_node = current_node.leftChild


    def find(self, value):

        current_node = self.root

        while current_node != None:
            if current_node.value == value:
                return True
            elif value > current_node.value:
                current_node = current_node.rightChild
            elif value < current_node.value:
                current_node = current_node.leftChild
        return False


    def traversePreOrder(self, root):
        #print(root)
        if root == None:
            return

        print(root.value)
        self.traversePreOrder(root.leftChild)
        self.traversePreOrder(root.rightChild)

    def traverseInOrder(self, root):
        if root == None:
            return

        self.traverseInOrder(root.leftChild)
        print(root.value)
        self.traverseInOrder(root.rightChild)
        
    def traversePostOrder(self, root):
        if root == None:
            return

        self.traverseInOrder(root.leftChild)
        self.traverseInOrder(root.rightChild)
        print(root.value)

    def traverseLevelOrder(self):
        for i in range(self.height(self.root) + 1)  :
            print(self.printKthNodes(self.root, i, []))
            # for val in self.printKthNodes(self.root, i):
            #     print(val)

        
    
    def height(self, root):
        if root == None:
            return -1
            
        if self.isLeaf(root):
            return 0

        return 1 + max(self.height(root.leftChild), self.height(root.rightChild))

    #O(log n) -> this is how we would perform the min action if using a binary search tree
    # in a binary search tree, the nodes are ordered so the entire left side is smaller than right
    def binaryMin(self):
        current = self.root
        last = current

        while current != None:
            last = current
            current = current.leftChild
        return last.value

    #O(n)
    def min(self, root):
        if root == None:
            return "tree is empty"

        
        if self.isLeaf(root):
            return root.value

        left = self.min(root.leftChild)
        right = self.min(root.rightChild)

        return min( min(left, right), root.value)

    def isLeaf(self, node):
        return node.leftChild == None and node.rightChild == None

    def equals(self, tree):
        return self.node_equals(self.root, tree.root)

    def node_equals(self, first, second):
        if first == None and second == None:
            return True

        if first != None and second != None:
            return (first.value == second.value) and (self.node_equals(first.leftChild, second.leftChild)) and (self.node_equals(first.rightChild, second.rightChild))

        return False

    def isBinarySearchTree(self, node, min=float('-inf'), max=float('inf')):
        if node == None:
            return True
        
        if node.value > min and node.value < max:        
            return self.isBinarySearchTree(node.leftChild, min=min, max=node.value) and self.isBinarySearchTree(node.rightChild, min=node.value, max=max)

        return False

    def printKthNodes(self, root, distance, node_list=[]):
        
        if distance == 0:
            node_list.append(root.value)
            return node_list

        if root == None:
            return

        self.printKthNodes(root.leftChild, distance - 1, node_list)
        self.printKthNodes(root.rightChild, distance - 1, node_list)

        return node_list

        

def main():
    tree = Tree()
    tree.insert(7)
    tree.insert(4)
    tree.insert(9)
    tree.insert(1)
    tree.insert(6)
    tree.insert(8)
    tree.insert(10)

    tree.traverseLevelOrder()

    # tree.isBinarySearchTree(tree.root)
    #print(tree.printKthNodes(tree.root, 1))

    # tree2 = Tree()
    # tree2.insert(7)
    # tree2.insert(4)
    # tree2.insert(9)
    # tree2.insert(1)
    # tree2.insert(6)
    # tree2.insert(8)
    # tree2.insert(10)
    # tree2.insert(30)

    # print(tree.equals(tree2))

    # print("Preorder:")
    # tree.traversePreOrder(tree.root)
    # print("In Order: ")
    # tree.traverseInOrder(tree.root)
    # print("Post Order: ")
    # tree.traversePostOrder(tree.root)
    print('Height: ')
    print(tree.height(tree.root))
    # print("Min Value: ", tree.min(tree.root))


if __name__ == "__main__":
    main()