class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0 
        count=0
        seen=set()
        while right<len(s):
            if s[right] not in seen:
                seen.add(s[right])
                count=max(count,len(seen))
                right+=1
            else:
                seen.remove(s[left])
                left+=1
        return count
