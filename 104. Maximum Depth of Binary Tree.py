# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ct=0
        def inorder(root,count):
            nonlocal ct
            if root is None:
                ct = max(ct,count)
                
                return
          
            inorder(root.left,count+1)
            inorder(root.right,count+1)

        inorder(root,0)

        return ct

        