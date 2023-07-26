def subs(str):
    
    if len(str) == 0:
        output = []
        output.append(" ")
        return output
    
    smallerString = str[1:]
    smallerOutput = subs(smallerString)
    
    output = []
    for sub in smallerOutput:
        output.append(sub)
        
    for sub in smallerOutput:
        subs_with_zeroth_char = str[0] + sub
        output.append(subs_with_zeroth_char)
    
    return output
    
print(subs("abc"))