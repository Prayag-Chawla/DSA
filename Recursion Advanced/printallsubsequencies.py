def printSub(str, output):
    if len(str) == 0:
        print(output)
        return
    
    # Not including 0th char
    printSub(str[1:], output)
    
    # Including 0th char
    printSub(str[1:], output+str[0])
     
printSub("abc", "")