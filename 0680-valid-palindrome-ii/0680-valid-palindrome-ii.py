class Solution:
    def palindrome(self,l,r,s):
        s1=s[l+1:r+1]
        s2=s[l:r]
        if s1==s1[::-1] or s2==s2[::-1]:
            return True
        else:
            return False

    def validPalindrome(self, s: str) -> bool:
        s=list(s)
        left=0
        right=len(s)-1
        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
                if left>=right:
                    return True
            if s[left]!=s[right]:
                r= self.palindrome(left,right,s)
                if r:
                    return True
                else:
                    return False
