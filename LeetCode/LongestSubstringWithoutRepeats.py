# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        substr = []
        for c in list(s):
            if c not in substr:
                substr.append(c)
            else:
                if max_len < len(substr):
                    max_len = len(substr)
                    
                while substr[0] != c:
                     substr.pop(0)
                        
                substr.pop(0)
                
                substr.append(c)
                
        if max_len < len(substr):
            max_len = len(substr)
            
        return max_len
