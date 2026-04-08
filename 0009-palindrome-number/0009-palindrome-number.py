class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        if(y[::-1]==y):
            return True
        else:
            return False
        