class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window_size=k
        window_sum=0
        for i in range(window_size):
            if blocks[i]=="W":
                window_sum+=1
        result=window_sum
        for i in range(window_size,len(blocks)):
            if blocks[i]=="W":
                window_sum+=1
            if blocks[i-window_size]=="W":
                window_sum-=1
            result=min(result,window_sum)
        return result