class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        new=[]
        if x[0]== "-" :
            new.append(x[0])
        x=x[::-1]
        for i in x:
            if i=="0":
                pass
            if i== "-":
                pass
            else:
                new.append(i)
        res_str="".join(str(n)for n in new)
        if int(res_str) < -2**31 or int(res_str) > 2**31 - 1:
            return 0
        else:
            return int(res_str)
    