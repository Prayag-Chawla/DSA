import queue

def checkRedundant(string):
    q=queue.LifoQueue()
    temp=0
    l=len(string)
    for i in range(l-1):
        c=string[i]
        n=string[i+1]
        if c=='(' and n==')':
            return True
        elif c=='(' and n=='(':
            temp=2
        elif c==')' and n==')' and temp==2:
            return True
    return False
#### Implement Your Code Here
    

string = input()
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')