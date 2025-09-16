# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def inorder(root,curr,target):
            if root is None:
                return False
                
            if root and root.left is None and root.right is None:
                if curr + root.val == target:
                    return True
                else:
                    return False

            if root:
                left = inorder(root.left,curr+root.val,target)
                right = inorder(root.right,curr + root.val,target)

                return left or right
        
        return inorder(root,0,targetSum)