# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        diff = True

        def dfs(node):
            if node is None:
                return 0
            nonlocal diff
            curr = node
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            if abs(left - right) > 1:
                diff = False
            
            return 1 + max(left, right)
        dfs(root)
        return diff
