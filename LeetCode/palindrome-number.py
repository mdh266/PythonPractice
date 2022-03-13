class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        s2 = s[::-1]
        return (s2 == s)
        