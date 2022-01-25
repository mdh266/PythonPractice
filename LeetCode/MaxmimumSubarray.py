# https://leetcode.com/problems/maximum-subarray

from typing import List
# brute force
cass Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        for i in range(len(nums)):
            test_sum = nums[i]
            for j in range(i+1, len(nums)):
                test_sum += nums[j]
                if test_sum > max_sum:
                    max_sum = test_sum
        return max_sum

# O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = float('-inf')
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum
                    