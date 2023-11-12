from stack import Stack

class StackQueue():
    def __init__(self, max) -> None:
        self.max = max
        self.count = 0
        self.enter_stack = Stack()
        self.exit_stack = Stack()

    def enqueue(self, item):

        if self.isFull():
            return "queue is full"

        self.enter_stack.push(item)
        self.count += 1

    def getExitOrder(self):
        while self.enter_stack.isEmpty() == False:
            self.exit_stack.push(self.enter_stack.pop())

    def dequeue(self):

        if self.isEmpty():
            return "queue is empty"

        if self.exit_stack.isEmpty():
            self.getExitOrder()

        removed = self.exit_stack.pop()
        self.count -= 1
        return removed

    def peek(self):
        if self.isEmpty():
            return None

        if self.exit_stack.isEmpty():
            self.getExitOrder()

        return self.exit_stack.peek()

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.max







def main():

    queue = StackQueue(max = 3)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.dequeue())


if __name__ == "__main__":
    main()