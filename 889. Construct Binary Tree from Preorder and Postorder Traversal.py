# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def recursive(ps,pe,pos,preorder,postorder):

            if ps > pe:
                return None
            if ps == pe:
                return TreeNode(preorder[ps])
            
            root=TreeNode(preorder[ps])
            i=1
            while postorder[pos+i-1] != preorder[ps+1]:
                i+=1
            root.left = recursive(ps+1,ps+i,pos,preorder,postorder)
            root.right = recursive(ps+i+1,pe,pos+i,preorder,postorder)
            return root

        return recursive(0,len(preorder)-1,0,preorder,postorder)

        

        