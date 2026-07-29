# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum_ = 0
        def calcsum(root, sum_, targetSum):
            if not root :
                return False
            if not root and sum_ ==targetSum:
                return True
           
            
            sum_+=root.val
            if not root.left and not root.right:
                return sum_ == targetSum
            if calcsum(root.left,sum_,targetSum):
                return True
            if calcsum(root.right,sum_,targetSum):
                return True
            sum_-=root.val
            return False
        return calcsum(root,sum_,targetSum)


        
        