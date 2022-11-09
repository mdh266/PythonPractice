# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    
        ans = [False]
        
        if root:
            self._hasPathSum(root, 0, targetSum, ans)
        
        return ans[0]
    
    def _hasPathSum(self, node, curr_sum, target_sum, ans):
        curr_sum += node.val
        
        if node.left is None and node.right is None:
            if curr_sum == target_sum:
                ans[0] = True
                
        if node.left:
            self._hasPathSum(node.left, curr_sum, target_sum, ans)

        if node.right:
            self._hasPathSum(node.right, curr_sum, target_sum, ans)
            

        
        
            

        
        