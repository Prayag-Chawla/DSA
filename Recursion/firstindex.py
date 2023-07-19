# def firstindex(arr, x):
#     size=len(arr)
#     if size<=0:
#         return -1
#     if x== arr[0]:
#         return 0
    
#     smallAns = firstindex(arr[1:], x)
#     if smallAns==-1:
#         return -1
#     else:
#         return smallAns+1
    
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# n=int(input())
# arr=list(int(i) for i in input().strip().split(' '))
# x=int(input())
# print(firstindex(arr, x))


def find_first_index(arr, x, index=0):
    # Base case: If index exceeds the array length, element not found
    if index >= len(arr):
        return -1

    # Base case: If element is found, return the current index
    if arr[index] == x:
        return index

    # Recursive case: Increment the index and search in the remaining array
    return find_first_index(arr, x, index + 1)


# Take input array from the user
arr = input("Enter the elements of the array (space-separated): ").split()
arr = [int(num) for num in arr]

# Take input integer from the user
x = int(input("Enter the integer to search for: "))

# Call the recursive function
result = find_first_index(arr, x)
print(result)


