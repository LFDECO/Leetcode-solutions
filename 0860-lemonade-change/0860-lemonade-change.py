class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        twen=0
        counter=0
        for i in bills:
            if i==5:
                five+=1
                counter+=1
            if i==10 and five>0:
                ten+=1
                five-=1
                counter+=1
            if i == 20:
                twen+=1
                if ten>=1 and five>=1:
                    ten-=1
                    five-=1
                    counter+=1
                elif ten<=0 and five>=3:
                    five-=3
                    counter+=1
                else:
                    break
                
        if counter==len(bills):
            return True
        else:
            return False
