class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    cnt = 0
    while head is not None:
        cnt += 1
    return cnt
        
def delete(head, i):
    if i < 0 or i > length(head):
        return head
    if i == 0:
        head = head.next
    else:
        curr = head
        for j in range(0, i):
            curr = curr.next
        end = curr.next.next
        curr.next.next = None
        curr.next = end       
        
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

arr=list(int(i) for i in input().strip().split(' '))

l = ll(arr[:-1])
i=int(input())
l = delete(l, i)
printll(l)