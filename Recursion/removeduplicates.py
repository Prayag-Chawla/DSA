def remove(string):
    if len(string)<=1:
        return string
    
    string2 = remove(string[1:])
    if string[0]==string[1]:
        return string2
    else:
        return string[0]+string2
    
string = input().strip()
print(remove(string))