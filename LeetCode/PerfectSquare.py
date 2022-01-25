# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        
        while i**2 <= num:
            if i**2 == num:
                return True
            else:
                i += 1
            
        return False