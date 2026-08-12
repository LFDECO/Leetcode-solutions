class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left=0
        right=len(people)-1
        count=0
        people.sort()
        while left<=right:
            if people[left]+people[right]<=limit:
                count+=1
                left+=1
                right-=1
            elif people[right]<=limit:
                count+=1
                right-=1
        return count