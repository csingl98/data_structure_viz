from queue import SimpleQueue

def reverse(queue):
    new_queue = SimpleQueue()
    #allowed methods: put, get, isEmpty
    #I'm mad bc I thought we weren't allowed to use a queue so I did it a more complicated way -_-
    reverse_list = []

    while queue.empty() != True:
        reverse_list.append(queue.get())
    
    index = len(reverse_list)

    while index >= 0:
        index -= 1
        new_queue.put(reverse_list[index])
        

    return new_queue


int_queue = SimpleQueue()
int_queue.put(10)
int_queue.put(20)
int_queue.put(30)

new_queue = reverse(int_queue)
print(new_queue.get())
