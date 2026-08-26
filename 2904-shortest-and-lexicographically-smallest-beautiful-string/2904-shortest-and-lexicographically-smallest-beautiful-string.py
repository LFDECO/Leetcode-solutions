class Solution:
    def shortestBeautifulSubstring(self, s: str, k: str) -> str:
   
        ones_idx = [i for i, ch in enumerate(s) if ch == '1']
        
      
        if len(ones_idx) < k:
            return ""
        
        ans = ""
        
     
        for i in range(len(ones_idx) - k + 1):
            start = ones_idx[i]
            end = ones_idx[i + k - 1]
            sub = s[start : end + 1]
           
            if not ans:
                ans = sub
            elif len(sub) < len(ans):
                ans = sub
            elif len(sub) == len(ans) and sub < ans:
                ans = sub
                
        return ans