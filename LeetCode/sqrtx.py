#https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i * i < x:
            i += 1
            
        if i * i == x:
            return i
        else: 
            return i -1