# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self,root):
            if not root:
                return []
            
            lst = self.inorder(root.left) + [root.val] + self.inorder(root.right)
            return lst

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # make an array of sorted values from BST
        # return kth index
        # if not root:
        #     return 
            
        # lst = self.kthSmallest(root.left,k) + [root.val] + self.kthSmallest(root.right,k)
        # if len(lst)==k:
        #     return lst[k-1]
        # return lst
        
        return self.inorder(root)[k-1]