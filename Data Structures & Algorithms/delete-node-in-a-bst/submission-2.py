class Solution:
    def minVal(self,root):
        curr = root
        while curr and curr.left:
            curr=curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None # NS
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.minVal(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right,minNode.val)
        return root