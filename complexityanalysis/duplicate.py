def MissingNumber(arr):
  sum1 = sum(arr)
  x = set()
  for i in arr:
    x.add(i)
  return sum1 - sum(x)
 

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
ans=MissingNumber(arr)
print(ans)