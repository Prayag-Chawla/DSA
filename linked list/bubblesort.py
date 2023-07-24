class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    cnt = 0
    while head:
        cnt += 1
        head = head.next
    return cnt

def ele(head, index):
    cnt = 0
    curr = head
    while curr:
        if cnt == index:
            return curr.data
        cnt += 1
        curr = curr.next
        
    return curr.data    
            
def swap_nodes(head, i, j):
  if ((i == 0 or j == 0) and (abs(i-j) == 1)): 

      curr1 = head
      head = head.next
      adv1 = head.next
      head.next = curr1
      curr1.next = adv1

  elif i == 0 or j == 0:
    if i == 0:
      curr1 = head
      ptr2 = head
      cnt = 1

      while cnt < j:
        cnt += 1
        ptr2 = ptr2.next

      curr2 = ptr2.next
       
      adv1 = curr1.next
      adv2 = curr2.next

      head = curr2
      curr2.next = adv1
      ptr2.next = curr1
      curr1.next = adv2

    elif j == 0:
      curr2 = head
      ptr1 = head
      cnt = 1

      while cnt < i:
        cnt += 1
        ptr1 = ptr1.next

      curr1 = ptr1.next
       
      adv2 = curr2.next
      adv1 = curr1.next

      head = curr1
      curr1.next = adv2
      ptr1.next = curr2
      curr2.next = adv1
    
  
  elif abs(i-j) == 1:
    if i < j:     
      cnt1 = 1
      cnt2 = 1
      ptr1 = head
      ptr2 = head

      while cnt1 < i:
        cnt1 += 1
        ptr1 = ptr1.next
      curr1 = ptr1.next
      adv1 = curr1.next

      while cnt2 < j:
        cnt2 += 1
        ptr2 = ptr2.next
      curr2 = ptr2.next
      adv2 = curr2.next
      
      ptr1.next = curr2
      curr2.next = curr1
      curr1.next = adv2

    elif j < i:     
      cnt1 = 1
      cnt2 = 1
      ptr1 = head
      ptr2 = head

      while cnt2 < j:
        cnt2 += 1
        ptr2 = ptr2.next
      curr2 = ptr2.next
      adv2 = curr2.next

      while cnt1 < i:
        cnt1 += 1
        ptr1 = ptr1.next
      curr1 = ptr1.next
      adv1 = curr1.next
      
      ptr2.next = curr1
      curr1.next = curr2
      curr2.next = adv1
  
  else:
      cnt1, cnt2 = 1,1
      ptr1, ptr2 = head, head
      while cnt2 < j:
        cnt2 += 1
        ptr2 = ptr2.next
      curr2 = ptr2.next
      adv2 = curr2.next

      while cnt1 < i:
        cnt1 += 1
        ptr1 = ptr1.next
      curr1 = ptr1.next
      adv1 = curr1.next

      ptr1.next = curr2
      curr2.next = adv1
      ptr2.next = curr1
      curr1.next = adv2

  return head
            
def bubbleSortLL(head):
    
    leng = length(head)
    
    for i in range(0, leng - 1):
        for j in range(0, leng - i - 1):       
            if ele(head,j) > ele(head,j+1):
                head = swap_nodes(head, j, j+1) 

    return head

                
        
def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
        
    return head
    
def printll(head):
    while head:
        print(head.data, end = " ")
        head = head.next
    print()
    
arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
l = bubbleSortLL(l)
printll(l)