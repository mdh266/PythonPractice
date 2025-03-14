# O(n) solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
   
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        val1, val2 = None, None
        index1, index2 = 0, len(nums)-1
        
        for i in range(len(nums)):
            val1 = nums[i]
            val2 = target - val1
            if val2 in d :
                if val1 != val2 or (val1 == val2 and d[val1] > 1):
                    index1 = i
                    break

        for i in range(len(nums)):
            if val2 == nums[i] and i != index1:
                index2 = i
                break

        return [index1, index2]


# another o(n) solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positions = {}
        for i, n in enumerate(nums):
            if n in positions:
                positions[n].append(i)
            else:
                positions[n] = [i]
        for n in nums:
            if target - n == n and len(positions[n]) > 1:
                return positions[n]
            if target - n != n and target-n in positions:
                return [positions[n][0], positions[target-n][0]]

# O(n^2)
# class Solution:          
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
#         
