
def check(L, R):
    if L == None and R == None:
        return True
    if L == None or R == None:
        return False
    left_val = check(L.left, R.right)
    right_val = check(L.right, R.left)
    return (L.val == R.val) and (left_val == True) and (right_val == True)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return True
        if root.left == None or root.right == None:
            return False
        result = check(root.left, root.right)
        return result