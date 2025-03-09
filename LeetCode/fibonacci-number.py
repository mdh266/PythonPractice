# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        vals = [0] * (n+1)
        
        if n >= 1:
            vals[1] = 1
        
        for i in range(2,n+1):
            vals[i] = vals[i-1] + vals[i-2]
            
        return vals[n]
                
        