# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        dummy = ListNode()
        curr1 = dummy
        for i in arr:
            curr1.next = ListNode(i)
            curr1 = curr1.next
        return dummy.next
