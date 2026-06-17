# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1=[]
        arr2=[]
        curr1=l1
        curr2=l2
        while curr1:
            arr1.append(str(curr1.val))
            curr1=curr1.next
        while curr2:
            arr2.append(str(curr2.val))
            curr2=curr2.next
        x1=int("".join(arr1))
        x2=int("".join(arr2))
        sum1=x1+x2
        res=list(str(sum1))
        dummy=ListNode()
        res1=dummy
        for i in res:
            res1.next=ListNode(int(i))
            res1=res1.next
        return dummy.next
            