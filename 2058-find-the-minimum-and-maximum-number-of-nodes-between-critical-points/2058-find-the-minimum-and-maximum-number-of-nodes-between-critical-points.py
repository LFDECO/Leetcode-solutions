# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = -1
        prev = -1

        min_dist = float('inf')
        max_dist = 0

        i = 1
        curr = head.next

        while curr.next:
            # local minimum OR local maximum
            if (curr.val < curr.next.val and curr.val < head.val) or \
               (curr.val > curr.next.val and curr.val > head.val):

                if first == -1:
                    first = i

                if prev != -1:
                    min_dist = min(min_dist, i - prev)
                    max_dist = i - first

                prev = i

            head = curr
            curr = curr.next
            i += 1

        if min_dist == float('inf'):
            return [-1, -1]

        return [min_dist, max_dist]