# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next is None and n == 1:
            head = None
            return

        count = 0
        curr = head
        while head.next is not None:
            if count >= n:
                curr = curr.next
                head = head.next
            else:
                head = head.next
                count += 1

        curr.val = curr.next.val
        curr.next = curr.next.next
