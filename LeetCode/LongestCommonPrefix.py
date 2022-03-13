# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(s) for s in strs])
        result = ""
        
        for i in range(min_len):
            next_char = list(set([s[i] for s in strs]))
            if len(next_char) > 1:
                break;
            else:
                result += next_char[0]
        
        return result


# or

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min([len(s) for s in strs])
        min_n = 0
        for i in range(n+1):
            if len(set([s[:i] for s in strs])) > 1:
                break;
            else:
                min_n = i
        return strs[0][:min_n]