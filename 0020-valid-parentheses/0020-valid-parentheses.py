class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        map1={"(":")","{":"}","[":"]"}
        counter=0
        if len(s)<=1:
            return False
        if s[0]==")" or s[0]=="}" or s[0] =="]":
            return False
        for i in s:
            if i=="(" or i=="{" or i =="[":
                stack.append(i)
            elif len(stack)>0 and map1[stack[-1]] == i:
                stack.pop()
            else:
                counter+=1
                break
            
        if len(stack)==0 and counter==len(stack):
            return True
        else:
            return False