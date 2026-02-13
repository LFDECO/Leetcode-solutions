class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        for i in range(len(temperatures)-2,-1,-1):
            j=i+1
            while(j<=len(temperatures)-1 and temperatures[j]<=temperatures[i] and result[j]!=0 ):
                j+=result[j]
            if j < len(temperatures) and temperatures[j] > temperatures[i]:
                result[i] = j - i
            else:
                result[i] = 0
        return result
        