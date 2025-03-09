# https://leetcode.com/problems/merge-sorted-array/submissions/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        
        while i < n and j < m:
            if nums2[i] < nums1[j]:
                temp = nums2[i]
                nums2[i] = nums1[j]
                nums1[j] = temp
                j += 1
                for z in range(i,n-1):
                    if nums2[z] > nums2[z+1]:
                        temp = nums2[z]
                        nums2[z] = nums2[z+1]
                        nums2[z+1] = temp
            else:
                j += 1
                
        for k in range(n-i):
            nums1[m + k] = nums2[i + k]