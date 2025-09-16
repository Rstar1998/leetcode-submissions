# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Definition for a binary tree node.
        temp =[]

        def inorder(root,arr,curr,target):
            nonlocal temp 

            if root is None:
                return False
                
            if root and root.left is None and root.right is None:
                if curr + root.val == target:
                    temp.append(arr + [root.val] )
                return 

            if root:
                left = inorder(root.left,arr+[root.val],curr+root.val,target)
                right = inorder(root.right,arr+[root.val],curr + root.val,target)

                return 
        inorder(root,[],0,targetSum)
        return temp