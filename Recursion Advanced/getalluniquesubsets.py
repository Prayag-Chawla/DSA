def find_unique_subsets(nums):
    def backtrack(start, path):
        unique_subsets.append(path[:])  

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue  

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    unique_subsets = []
    nums.sort()  # Sort the input array (if not already sorted)
    backtrack(0, [])
    return unique_subsets

arr = [1, 2, 2]
result = find_unique_subsets(arr)
print(result)
