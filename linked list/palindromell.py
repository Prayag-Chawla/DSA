class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printll(head):
  list = []
  while head is not None:
    list.append(head.data)
    head = head.next
  return list
  
def reverseLL(head):
  list = []
  while head is not None:
    list.insert(0, head.data) 
    head = head.next
  return list


def check_palindrome(head):
  
  if printll(head)  == reverseLL(head):
    return True
  else:
    return False   
    
    
    

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
ans = check_palindrome(l)
if ans:
    print("true")
else:
    print("false")