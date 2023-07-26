import queue

class StackUsingQueues:
    def __init__(self):
        self.queue1 = queue.Queue()
        self.queue2 = queue.Queue()
        self.current_size = 0

    def push(self, data):
        self.queue1.put(data)
        self.current_size += 1

    def pop(self):
        if self.isEmpty():
            return -1

        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        
        element = self.queue1.get()
        self.current_size -= 1

        # Swap queues to maintain the stack behavior
        self.queue1, self.queue2 = self.queue2, self.queue1

        return element

    def top(self):
        if self.isEmpty():
            return -1

        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        
        top_element = self.queue1.get()
        self.queue2.put(top_element)

        # Swap queues to maintain the stack behavior
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def size(self):
        return self.current_size

    def isEmpty(self):
        return self.current_size == 0

# Example usage:
stack = StackUsingQueues()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.top())  # Output: 3
print(stack.pop())  # Output: 3
print(stack.size())  # Output: 2
print(stack.isEmpty())  # Output: False
