# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        vals = [0] * (n+1)
        
        if n >= 1:
            vals[1] = 1
        if n >= 2:
            vals[2] = 1
        if n > 2:
            for i in range(3,n+1):
                vals[i] = vals[i-3] + vals[i-1] + vals[i-2]
                
        return vals[n]