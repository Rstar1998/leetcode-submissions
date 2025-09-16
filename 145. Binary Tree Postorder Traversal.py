# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out=[]
        
        def inorder(root):
            nonlocal out

            if root:
                
                inorder(root.left)
                inorder(root.right)
                out.append(root.val)

        inorder(root)

        return out  

        