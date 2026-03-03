class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        x=sum(gas)
        y=sum(cost)
        start=0
        current_fuel=0
        total=0
        if x<y:
            return -1
        for i in range(len(gas)):
            current_fuel+=gas[i]-cost[i]
            if current_fuel<0:
                current_fuel=0
                start=i+1
                continue
            
            
        return start
