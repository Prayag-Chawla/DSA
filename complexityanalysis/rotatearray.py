def Rotate(arr, d):
    d = d % len(arr)
    for i in range(d, len(arr)):
        print(arr[i], end=" ")
    for i in range(0, d):
        print(arr[i], end=" ")
            

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
d=int(input())
Rotate(arr, d)