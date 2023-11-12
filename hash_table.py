from linked_lists import LinkedList

# HashTable
# put
# get
# remove
# keys: integers, values: strings
# Collisions: chaining
# Create a new class Entry That Makes a Linked List Array
#

class Entry():
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class HashTable():
    def __init__(self, max) -> None:
        #array of LinkedLists: [LL, LL, LL, LL]
        # each Linked List holds and Entry object LL.value = Entry(k, v)
        self.max = max
        self.hash_array = [LinkedList() for i in range(self.max)]

    def hash(self, k):
        return k % self.max

    def put(self, k, v):
        entry = Entry(k, v)

        #hash key to get index
        index = self.hash(k)
        linked_list = self.hash_array[index]

        #if value is already in node, update Node, else add new node
        if self.findValue(linked_list, k) == None:
            linked_list.addLast(entry)
            return

        for entry in linked_list.toArray():
            if entry.key == k:
                entry.value = v
        return


    def get(self, k):
        index = self.hash(k)
        linked_list = self.hash_array[index]
        return self.findValue(linked_list, k)
        

    def findValue(self, linked_list, k):

        for entry in linked_list.toArray():
            if entry.key == k:
                return entry.value

        return None


    def remove(self, k):
        index = self.hash(k)
        linked_list = self.hash_array[index]
        removed = None

        #create new linked list without the one that has been removed
        new_list = LinkedList()
        for link in linked_list.toArray():
            entry = link.value
            if entry.key != k:
                new_list.addLast(entry)
            else:
                removed = entry.value
        
        self.hash_array[index] = new_list
        return removed


def main():
    table = HashTable(max=5)
    table.put(6, "A")
    table.put(8, "B")
    table.put(11, "C")

    print("Done")


if __name__ == "__main__":
    main()