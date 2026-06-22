class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        sum1=0
        for i in costs:
            sum1+=i
            if sum1<coins or sum1==coins:
                count+=1
            else:
                break
        return count