class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        sum_evens = sum([val for val in d.values() if val % 2 == 0])
        odds_minus_1 = [val-1 for val in d.values() if val % 2 == 1] # subtract 1
        if len(odds_minus_1) > 0:
            max_odds = sum(odds_minus_1) + 1
        else:
            max_odds = 0

        return sum_evens + max_odds