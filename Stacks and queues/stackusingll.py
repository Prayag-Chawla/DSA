# THis is the developers side code and we're making head and cnt as private
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.__head = None
        self.__cnt = 0
        
    def push(self, element):
        newNode = Node(element)
        newNode.next = self.__head
        self.__head = newNode
        self.__cnt += 1
        
        
    def pop(self):
        if self.isEmpty() is True:
            print("Hey! Stack is Empty!!")
            return
        
        data = self.__head.data
        self.__head = self.__head.next
        self.__cnt -= 1
        
        return data
        
    def top(self):
        if self.isEmpty() is True:
            print("Hey! Stack is Empty!!")
            return
        
        return self.__head.data
    
    def size(self):
        return self.__cnt
        
    def isEmpty(self):
        return self.size() == 0         # return self.__head is None      // You can sue this as well
s= Stack()

s.push(10)
s.push(20)
s.push(30)

while s.isEmpty() is False:
    print(s.pop())
s.top()        