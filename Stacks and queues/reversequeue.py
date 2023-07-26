import queue

def reverse_queue(queue):
    if queue.empty():
        return

    front_element = queue.get()
    reverse_queue(queue)
    queue.put(front_element)


q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)

print("Original Queue:")
while not q.empty():
    print(q.get(), end=" ")

reverse_queue(q)

print("\nReversed Queue:")
while not q.empty():
    print(q.get(), end=" ")
