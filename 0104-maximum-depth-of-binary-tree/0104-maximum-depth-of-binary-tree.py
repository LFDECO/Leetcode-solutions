# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def dfs(node):
            if node is None:
                return 0
            else:
                return 1+max(dfs(node.left),dfs(node.right))
        result=dfs(root)
        return result    