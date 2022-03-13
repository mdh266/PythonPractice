# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
		d = {
			 ")": "(",
		     "]": "[",
		     "}": "{"}

		stack = []

		if len(s) % 2 != 0:
			return False

		for c in s:
			if c in d.keys():
				if stack.pop() != d[c]:
					return False
			else:
				stack.append(c)
		return True
