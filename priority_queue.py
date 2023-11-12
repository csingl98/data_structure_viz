
class PriorityQueue():
    def __init__(self, max) -> None:
        self.first = 0
        self.last = 0
        self.max = max
        self.count = 0
        self.queue = [None for i in range(self.max)]

    def enqueue(self, item):

        if self.isFull():
            return "queue is full"

        index = self.count - 2
        self.count += 1

        while index >= 0:
            current_num = self.queue

            if current_num > item:
                self.queue[index + 1] = current_num
                
            else:
                self.queue[index + 1] = item
                return
        
        self.queue[0] = item
        return




    def dequeue(self):

        if self.isEmpty():
            return "queue is empty"

        self.count -= 1
        removed = self.queue[self.count]

        return removed

    def peek(self):
        if self.isEmpty():
            return None

        return self.queue[self.first]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.max
        


def main():
    pass

if __name__ == "__main__":
    main()
