class Solution:
    def isPalindrome(self, x: int) -> bool:
        y1=str(x)
        if(y1[::-1]==y1):
            return True
        else:
            return False
        