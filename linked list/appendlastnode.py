class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    cnt = 0
    while head is not None:
        cnt += 1
        head = head.next
    return cnt

        
def append_LinkedList(head,n) :
    if n == 0:
        return None
    
    pos = length(head) - n
    curr = head
    prev = head
    
    for i in range(1,pos):
        curr = curr.next
    
    last = curr
    temp = curr.next
    head = temp
    
    while curr.next is not None:
        curr = curr.next
    curr.next = prev
    last.next = None
    
    return head
    


def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = append_LinkedList(l, i)
printll(l)