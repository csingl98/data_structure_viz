
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def addFirst(self, value):

        add_node = Node(value)

        if self.isEmpty():
            self.head = self.tail = add_node

        else:
            add_node.next = self.head
            self.head = add_node
        self.length += 1


    def addLast(self, value):
        
        add_node = Node(value)

        if self.head == None:
            self.head = self.tail = add_node

        else:
            self.tail.next = add_node
            self.tail = add_node

        self.length += 1

    def deleteFirst(self):
        if self.head == None and self.tail == None:
            #list is empty 
            return Exception

        if self.head == self.tail:
            self.head == self.tail == None
        else:
            #simply set the node aat self.head.next to be the new head node
            new_head = self.head.next
            self.head.value = new_head.value
            self.head.next = new_head.next
        self.length -= 1

    def deleteLast(self):
        if self.head == None and self.tail == None:
            #list is empty 
            return Exception

        current_node = self.head
        while current_node.next != None:
            if current_node.next == self.tail:
                self.tail.value = current_node.value
                self.tail.next = None
                
            current_node = current_node.next
        self.length -= 1


    def contains(self, value):
        while current_node.next != None:
            if current_node.value == value:
                return True
                
            current_node = current_node.next

        return False

    def indexOf(self, value):

        index = 0
        current_node = self.head
        while current_node.next != None:
            if current_node.value == value:
                return index
                
            current_node = current_node.next
            index += 1

        return -1

    def size(self):
        return self.length

    def toArray(self):
        array = []
        current = self.head

        while current != None:
            array.append(current.value)
            #print(current.value)
            current = current.next

        return array


    def print(self):

        current_node = self.head
        while current_node != None:
            print(current_node.value)
            current_node = current_node.next

    def reverse(self):

        if self.isEmpty():
            return None
        
        previous = None
        current = self.head

        while current!= None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous


    def getKthFromTheEnd(self, k):
        #declare 2 pointers
        first = self.head
        second = self.head.next 
        #set a variable to keep track of distance
        distance = 0

        if self.isEmpty():
            return None

        if k > self.length or k < 1:
            return IndexError

        while second != None:

            if distance != k-1:
                second = second.next
                distance +=1

            else:
                first = first.next
                second = second.next

        return first.value

    def printMiddle(self):

        first = self.head
        second = self.head.next
        counter = 0

        #move second pointer to the end

        #keep a counter to keep trak of where we are in the list

        #once we hit the end, divide the count in half and move first forward that many nodes
        while second != None:
            second = second.next
            counter += 1

        middle = counter/2
        


        

# list = LinkedList()
# list.addLast(10)
# list.addLast(20)
# list.addLast(30)
# list.addLast(40)
# list.addLast(50)
# #list.deleteFirst()
# #list.print()
# #list.deleteFirst()
# #list.print()
# print(list.size())
# print(list.toArray())
# list.reverse()
# print(list.toArray())
# print(list.getKthFromTheEnd(3))

