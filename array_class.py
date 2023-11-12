
#pretend this is like Java and arrays have to be copied
class Array():

    def __init__(self, length) -> None:
        self.length = 0
        self.values = [None for i in range(length)]

    def print(self):
        for i in range(self.length):
            print(self.values[i])

    def insert(self, num):
        if self.length == len(self.values):
            new_size = self.length * 2
            new_items = [None for i in range(new_size)]

            for i in range(self.length):
                new_items[i] = self.values[i]
            
            self.values = new_items
      
        self.values[self.length] = num
        self.length += 1
        
        return self.values

    def removeAt(self, index):     

        if index >= 0 and index < self.length:           
            self.length = self.length - 1
            new_items = [None for i in range(self.length)]

            n=0
            for i in range(self.length + 1):

                if i == index:
                    continue

                new_items[n] = self.values[i]
                n += 1

            self.values = new_items

            return self.values

        else: 
            return Exception

    def indexOf(self, num):

        for i in range(self.length):
            if self.values[i] == num:
                return i

        return -1

numbers = Array(length=5)
numbers.print()
numbers.insert(10)
numbers.insert(20)
numbers.insert(30)
numbers.print()
print("index of 30: ", numbers.indexOf(30))
numbers.removeAt(0)
print("after removing: ")
numbers.print()
print("index of 30: ", numbers.indexOf(30))