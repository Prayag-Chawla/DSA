def find_last_index(arr, x, index):
    # Base case: If index reaches -1, element not found
    if index == -1:
        return -1

    # Base case: If element is found, return the current index
    if arr[index] == x:
        return index

    # Recursive case: Decrement the index and search in the remaining array
    return find_last_index(arr, x, index - 1)


# Take input array from the user
arr = input("Enter the elements of the array (space-separated): ").split()
arr = [int(num) for num in arr]

# Take input integer from the user
x = int(input("Enter the integer to search for: "))

# Call the recursive function, starting from the last index (N-1)
result = find_last_index(arr, x, len(arr) - 1)
print(result)
