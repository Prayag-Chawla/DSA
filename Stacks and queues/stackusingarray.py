class Stack:
    def __init__(self):
        self.__data = []       #Private array: not to give access to the user
    
    def push(self, item):
        self.__data.append(item)
        
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty!")
            return
        return self.__data.pop()
    
    def top(self):
        if self.isEmpty():
            print("Stack is Empty!")
            return
        return self.__data[len(self.__data) - 1]
    
    def size(self):
        return len(self.__data)
        
    def isEmpty(self):
        return self.size() == 0
#### This part is visible to the user
## Actually we need to write the above program in another fila and here in the below code we can import the Stack class using import statement

# from _11.2StackUsingArray import Stack

s = Stack()

s.push(12)
s.push(13)
s.push(14)

while s.isEmpty() is False:
    print(s.pop())
s.top()        
