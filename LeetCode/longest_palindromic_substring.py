# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
            

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        curr = ""
        for c in range(len(s)):
            curr = self.expand(s, c, c)
            if len(curr) >= len(longest):
                longest = curr

            curr = self.expand(s, c, c+1)
            if len(curr) >= len(longest):
                longest = curr

        return longest
