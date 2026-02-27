1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        result=[]
4        left = 0
5        right = len(numbers)-1
6        while(left<=right):
7            if numbers[left]+numbers[right]==target:
8                result.extend([left+1,right+1])
9                break
10            if numbers[left]+numbers[right]<target:
11                left+=1
12            if numbers[left]+numbers[right]>target:
13                right-=1
14        return result