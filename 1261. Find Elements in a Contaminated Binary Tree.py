# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.hash = set()
        def traverse(node,level):
            node.val = level
            self.hash.add(level)
            if node.left is None and node.right is None:
                return
            
            if node.left:
                traverse( node.left, 2*level+1)
            if node.right:
                traverse( node.right, 2*level+2)

        traverse(root,0)

    def find(self, target: int) -> bool:
        if target in self.hash:
            return True
        else:
            return False

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)