import math
from turtle import left, right



class Heap():
    def __init__(self) -> None:
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1

        self.bubbleUp(index)

    def isSmallerThanParent(self, index):
        if index == 0:
            return True

        parent = self.getParentValue(index)

        return self.heap[index] <= parent

    def isGreaterThanChildren(self, index):
        largest_child, child_index = self.getLargestChild(index)

        if largest_child == None:
            #leaf node
            return True
        
        return self.heap[index] >= largest_child

    def getLargestChild(self, index):
        left_child = self.heap[self.getLeftChildIndex(index)] if self.getLeftChildIndex(index) < len(self.heap) else None
        right_child = self.heap[self.getRightChildIndex(index)] if self.getRightChildIndex(index) < len(self.heap) else None

        if right_child == None or left_child > right_child:
            return left_child, self.getLeftChildIndex(index)
        else:
            return right_child, self.getRightChildIndex(index)

    def getParentValue(self, index):
        return self.heap[self.getParentIndex(index)]

    def getChildValues(self, index):
        left_child = self.getLeftChildIndex(index) if self.getLeftChildIndex(index) < len(self.heap) else None
        right_child = self.getRightChildIndex(index) if self.getRightChildIndex(index) < len(self.heap) else None
        
        return left_child, right_child

    def getLeftChildIndex(self, index):
        return (index * 2) + 1

    def getRightChildIndex(self, index):
        return (index * 2) + 2

    def getParentIndex(self, index):
        return int((index - 1) / 2)

    def remove(self):
        self.heap[0] = self.heap.pop()
        self.bubbleDown(0)

    def bubbleUp(self, index):
        if self.isSmallerThanParent(index):
            return

        parent = self.getParentValue(index)
        parent_index = self.getParentIndex(index)
        self.heap[parent_index] = self.heap[index]
        self.heap[index] = parent
        self.bubbleUp(parent_index)

    def bubbleDown(self, index):
        if self.isGreaterThanChildren(index):
            return
        
        largest_child, child_index = self.getLargestChild(index)
        self.heap[child_index] = self.heap[index]
        self.heap[index] = largest_child
        self.bubbleDown(child_index)


def heapify(array):
    #[20, 30, 10, 40, 50] -> [50, 40, 30, 20, 10]

    #formula for finding the last parent node in a heap
    i = len(array) / 2 - 1
    while i >= 0:

        heapify(array, i)
        i-= 1

        
def heapify(array, i):
    left_index = (i * 2) + 1
    left_child = array[left_index] if left_index < len(array) else float('-inf')

    right_index = (i * 2) + 2
    right_child = array[right_index] if right_index < len(array) else float('-inf')

    if left_child > right_child:
        largest_child = left_child
        largest_index = left_index
    else:
        largest_child = right_child
        largest_index = right_index

    if array[i] < largest_child:
        array[largest_index] = array[i]
        array[i] = largest_child
        heapify(largest_index)
    else:
        return

def findKthLargest(array, k):
    heap = Heap()
    for num in array:
        heap.insert(num)

    kth_largest = 0
    for n in range(k - 1):
        heap.remove()

    return heap.heap[0]

def main():
    numbers = [5, 3, 8, 4, 1, 2]

    #using a heap to find kth largest 


    heap = Heap()


    print("Done")

if __name__ == '__main__':
    main()