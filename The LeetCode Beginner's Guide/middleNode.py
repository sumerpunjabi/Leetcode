# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        middle = length // 2
        node = head

        while middle > 0:
            middle -= 1
            node = node.next

        return node