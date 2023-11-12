
class ArrayQueue():
    def __init__(self, max) -> None:
        self.first = 0
        self.last = 0
        #in Mosh's code he used a count variable to keep track of length rather than using first and last
        #honestly I should probably just use lists instead of pointers since this is python
        self.max = max
        self.count = 0
        self.queue = [None for i in range(self.max)]

    def enqueue(self, item):

        if self.isFull():
            return "queue is full"

        self.queue[self.last] = item
        self.count += 1
        self.last = (self.last + 1) % self.max


    def dequeue(self):

        if self.isEmpty():
            return "queue is empty"

        removed = self.queue[self.first]
        self.queue[self.first] = None
        self.count -= 1
        self.first = (self.first + 1) % self.max


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
    queue = ArrayQueue(max = 3)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(60)
    print(queue.dequeue())


if __name__ == "__main__":
    main()
