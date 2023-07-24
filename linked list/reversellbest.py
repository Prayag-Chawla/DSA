class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
   
    
def printll(head):
    while head is not None:
        print(head.data, "-->", end = " ")
        head = head.next
    print("None")
        
def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head  

def reverse3(head):    
    if head is None or head.next is None:
        return head
    smallHead = reverse3(head.next)
    # tail = head.next
    # tail.next = head
    # The above 3 lines can be written in one line as the following
    head.next.next = head
    head.next = None
    
    return smallHead


#arr = list(int(x) for x in input().split())
arr = [1,2,3,4,5,-1]
l = ll(arr[:-1])
printll(l)

head = reverse3(l)
printll(head)