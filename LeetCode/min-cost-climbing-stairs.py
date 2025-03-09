# https://leetcode.com/problems/min-cost-climbing-stairs

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincosts = [0]*len(cost)
        mincosts[0] = cost[0]
        mincosts[1] = cost[1]
 
        for i in range(2,len(cost)):
            mincosts[i] = cost[i] + min(mincosts[i-1], mincosts[i-2])
        
        return min(mincosts[-1],mincosts[-2])
        
