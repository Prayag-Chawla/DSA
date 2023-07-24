class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge(head1,head2):

    fh = Node(3)
    ft = fh       
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            ft.next = head1
            ft = ft.next
            head1 = head1.next
        else:
            ft.next = head2
            ft = ft.next
            head2 = head2.next
            
    while head1 is not None:
        ft.next = head1
        ft = ft.next
        head1 = head1.next
    
    while head2 is not None:
        ft.next = head2
        ft = ft.next    
        head2 = head2.next
    
    return fh.next

def midpoint_linkedlist(head):
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def mergeSort(head):
    if head.next is None:
      return head

    mid = midpoint_linkedlist(head)

    h1 = head
    temp = head
    while temp is not mid:
        temp = temp.next
    h2 = temp.next       
    temp.next = None

    h1 = mergeSort(h1)
    h2 = mergeSort(h2)
    
    return merge(h1, h2)


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
l = mergeSort(l)
printll(l)