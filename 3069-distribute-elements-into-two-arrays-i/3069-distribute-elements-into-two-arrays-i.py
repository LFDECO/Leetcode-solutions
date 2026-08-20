class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[]
        arr2=[]
        arr1.append(nums[0])
        arr2.append(nums[1])
        counter1=len(arr1)-1
        counter2=len(arr2)-1
        for i in range(2,len(nums)):
            if arr1[counter1]>arr2[counter2]:
                arr1.append(nums[i])
                counter1+=1
            else:
                arr2.append(nums[i])
                counter2+=1
        return arr1+arr2