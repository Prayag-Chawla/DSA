class Stack:
    def __init__(self):
        self.__data = []
    
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
def checkBalanced(str):           
    for i in str:
        if i == '(' or i == '{' or i == '[':
            s.push(i)
            
        elif i =='}':
            if s.top() != '{':
                return False
            s.pop()
        elif i == ']':
            if s.top() == '[':
                return False
            s.pop()
        elif i == ')':
            if s.top() == '(':
                return False
            s.pop()
            
            
    if s.isEmpty():
        return True
    else:
        return False
    
s= Stack()

exp = input()
#exp = "{x + y ( a * b )  }"
if checkBalanced(exp):
    print('true')
else:
    print('false')

    