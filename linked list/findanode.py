class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linearsearch(head, n):
    curr = head
    cnt = 0
    while curr is not None:
        if curr.data == n:
            return cnt
        cnt += 1
        curr = curr.next

    return -1

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1: ]:
        last.next = Node(data)
        last = last.next

    return head

arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
data=int(input())
index = linearsearch(l, data)
print(index)

    