def find_unique(li, n):
    for i in range(n):
        for j in range(0, n):
            if i == j:
                continue
            if(li[i] == li[j] and j == n):
                return li[i]


n = 7
li = [2, 3, 1, 6, 3, 6, 2]
ele = find_unique(li, n)
print(ele)