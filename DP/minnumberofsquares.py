import sys
def minStepsTo1(n):
    
    dp = [0 for i in range(n+1)]
    
    for i in range(1,n+1):
        dp[i] = sys.maxsize
        for j in range(1,i+1):
            temp = j*j
            if temp > i:
                break
            dp[i] = min(dp[i],1+dp[i-temp])
    
    ans = dp[n]
    return ans
        

    
n = int(input())
ans = minStepsTo1(n)