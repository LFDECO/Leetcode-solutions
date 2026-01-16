class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0
        for i in range (len(heights)):
            if len (stack)==0 or heights[i]>heights[stack[-1]]:
                stack.append(i)
            else:
                   while(stack and heights[i]<heights[stack[-1]]):
                        stored=stack.pop()
                        if len(stack)==0:
                            width=i
                            area=heights[stored]*width
                            maxarea=max(maxarea,area)
                        else:
                            width=i-stack[-1]-1
                            area=heights[stored]*width
                            maxarea=max(maxarea,area)
            stack.append(i)
        n=len(heights)
        while(len(stack)!=0):
            stored=stack.pop()
            if len(stack)==0:
                width=n
                area=heights[stored]*width
                maxarea=max(maxarea,area)
            else:
                width=n-stack[-1]-1
                area=heights[stored]*width
                maxarea=max(maxarea,area)
        return maxarea
                    
                