import queue

def reverse_k_elements(queue, k):
    if queue.empty() or k <= 0:
        return

    stack = []
    count = 0

    # Dequeue the first K elements and store them in the stack
    while count < k and not queue.empty():
        stack.append(queue.get())
        count += 1

    # Enqueue the elements from the stack back into the queue in reverse order
    while stack:
        queue.put(stack.pop())

    # Move the remaining (size - k) elements to the end of the queue
    for _ in range(queue.qsize() - k):
        queue.put(queue.get())


q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

print("Original Queue:")
while not q.empty():
    print(q.get(), end=" ")

q = queue.Queue()  

q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

reverse_k_elements(q, 3)

print("\nReversed First 3 Elements:")
while not q.empty():
    print(q.get(), end=" ")
