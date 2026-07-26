# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        answer = []
        if not root:
            return []
        # answer.append([root.val])
        queue.append(root)
        level = 0
        while len(queue)>0:
            mini_ans = []
            for i in range(len(queue)):
                node = queue.popleft()
                mini_ans.append(node.val)
                if node.left:
                   
                    queue.append(node.left)
                if node.right:
                    
                    queue.append(node.right)
            level+=1
            answer.append(mini_ans)
        return answer

                



        