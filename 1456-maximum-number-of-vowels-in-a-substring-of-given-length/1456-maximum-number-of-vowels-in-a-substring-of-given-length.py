class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window_size=k
        window_sum=0
        for i in range(window_size):
            if s[i] in "aeiou":
                window_sum+=1
        result=window_sum
        for i in range(window_size,len(s)):
            if s[i] in "aeiou":
                window_sum+=1
            if s[i-window_size] in "aeiou":
                window_sum-=1
            result=max(result,window_sum)
        return result