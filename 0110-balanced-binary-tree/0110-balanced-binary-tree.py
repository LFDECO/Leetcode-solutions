# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def height(node):
    if node is None:
        return 0
    left=height(node.left)
    right=height(node.right)
    return 1+max(left,right)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_height=height(root.left)
        right_height=height(root.right)
        if abs(left_height-right_height)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
