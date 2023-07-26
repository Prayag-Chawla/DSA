def permutation(str):
    if len(str) == 0:
        return 
    
    output = []
    for i in range(len(str)):
        
        start = str[i]
        
        remaining = str[:i] + str[i+1:]        
        permutation(remaining)
        output.append(start + remaining)
        
        next1 = remaining[::-1]
        permutation(next1)
        output.append(start + next1 )
        
    return output

print(permutation("abcd"))
    