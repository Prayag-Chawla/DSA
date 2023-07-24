
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head, i, j):
    
    ptr1 = head
    ptr2 = head
    
    cnt1 = 0
    cnt2 = 0
    
    while cnt1 < i:
        cnt1 += 1
        ptr1 = ptr1.next
        
    while cnt2 < j:
        cnt2 += 1
        ptr2 = ptr2.next
        
    curr1 = ptr1
    curr2 = ptr2
    
    data1 = curr1.data
    data2 = curr2.data

    curr1.data = data2
    curr2.data = data1

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
i, j=list(int(i) for i in input().strip().split(' '))
l = swap_nodes(l, i, j)
printll(l)