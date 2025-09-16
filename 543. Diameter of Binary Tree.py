# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mx= 0
        def inorder(root):
            nonlocal mx
           
            if root.left is None and root.right is None:
                return 1

            left = 0
            right = 0
            if root.left is not None:
                left = inorder(root.left)
            if root.right is not None:
                right = inorder(root.right)
            mx = max(mx , left +right)

            return max(left+1 , right+1)
        inorder(root)
        return mx



        