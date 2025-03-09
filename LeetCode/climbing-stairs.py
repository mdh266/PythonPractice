# https://leetcode.com/problems/climbing-stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n = 1
        1
        
        n = 2
        1 + 1
        2
        outcome = 2
        
        n = 3
        1 + 1 + 1
        2 + 1
        1 + 2
        
        outcome = 3
        
        n = 4
        1 + 1 + 1 + 1
        2 + 1 + 1
        1 + 1 + 2
        1 + 2 + 1
        2 + 2
        
        output = 5
        
        n = 5
        1 + 1 + 1 + 1 + 1
        2 + 2 + 1 
        1 + 2 + 2
        2 + 1 + 2
        1 + 1 + 1 + 2
        2 + 1 + 1 + 1
        1 + 1 + 2 + 1
        1 + 2 + 1 + 1
        
        output = 8
        """
        vals = [0]*n
        vals[0] = 1
        if n > 1:
            vals[1] = 2
            for i in range(2,n):
                vals[i] = vals[i-1] + vals[i-2]

        return vals[n-1]
 
            

            


