class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linkedlist_spl(head):

  if head is None:
    return None
   
  return print_linkedlist_spl(head.next), print(head.data, end = " ")    
    

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


from sys import setrecursionlimit
setrecursionlimit(10000)
arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
print_linkedlist_spl(l)