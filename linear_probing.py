
#HASHMAP USING ONLY ARRAYS AND LINEAR PROBING
class HashMap():

    def __init__(self, length) -> None:
        #an array of tuples or arrays to store (key, value)
        self.values = [None] * length

    def put(self, key, value):

        index = self.handleCollision(self.hash(key))
        self.values[index] = [key, value]

    def get(self, key):
        
        index = self.findKey(self.hash(key), key)

        if index == None:
            return None

        return self.values[index][1]
    
    def hash(self, key: str):
        return hash(key) % len(self.values)

    def remove(self, key):
        index = self.findKey(self.hash(key), key)

        if index == None:
            return None

        value = self.values[index][1]
        self.values[index] = None

        return value

    def size(self):
        return len(self.values)

    def isEmpty(self, index):
        return self.values[index] == None

    def handleCollision(self, index):
        #check size first
        if self.isFull():
            self.doubleSize(len(self.values))
        
        for i in range(len(self.values)):
            new_index = index + i
            if new_index >= len(self.values):
                new_index -= len(self.values)

            if self.isEmpty(new_index):
                return new_index

    def findKey(self, index, key):

        for i in range(len(self.values)):
            new_index = index + i
            if new_index >= len(self.values):
                new_index -= len(self.values)

            if self.values[new_index] == None:
                continue
            
            if self.values[new_index][0] == key:
                return new_index

        return None

    def isFull(self):
        return None not in self.values

    def doubleSize(self, length):
        new_table = HashMap(length * 2)
        for values in self.values:
            if values == None:
                continue

            new_table.put(values[0], values[1])

        self.values = new_table.values


def main():
    hashmap = HashMap(5)
    hashmap.put("One", 1)
    hashmap.put("Two", 2)
    hashmap.put("Three", 3)
    hashmap.put("Five", 5)
    hashmap.put("Six", 6)
    #hashmap.put("Seven", 7)
    print(hashmap.get("Six"))
    hashmap.remove("Six")
    print(hashmap.get("Six"))
    hashmap.put("Four", 4)


if __name__ == "__main__":
    main()



