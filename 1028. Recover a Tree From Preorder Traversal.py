# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        root = None
        i = 0
        st=[]
        while i < len(traversal):
            d=0
            while i < len(traversal) and traversal[i] == '-':
                d+=1
                i+=1
            
            num=""
            while i < len(traversal)  and traversal[i].isdigit():
                num+=traversal[i]
                i+=1
        
            num=int(num)

            node = TreeNode(num)

            while len(st) > d:
                st.pop()
            
            if len(st) > 0:
                if not st[-1].left:
                    st[-1].left = node
                else:
                    st[-1].right =node
            else:
                root=node
            
            st.append(node)
        return root






   

      
        