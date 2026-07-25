class Solution:
    
    def minVal(self,root):
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val :
            root.right = self.deleteNode(root.right, key)
        elif key< root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                minNode = self.minVal(root.right)
                root.val = minNode
                root.right = self.deleteNode(root.right,minNode)
        return root


            
