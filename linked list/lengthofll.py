class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    curr = head
    cnt = 0
    while curr is not None:
        cnt += 1
        curr = curr.next
        
    return cnt

def ll(arr):
    print(arr)
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
len=length(l)
print(len)

