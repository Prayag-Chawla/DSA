from sys import stdin

def arrayEquilibriumIndex(arr,n):
  
    n=len(arr)
    leftsum=0
    rightsum=0
    for i in range(n):
        rightsum+=arr[i]
    for i in range(n):
      rightsum-=arr[i]
      if leftsum==rightsum:
            return i
      leftsum+=arr[i]
    return -1 


def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t-= 1