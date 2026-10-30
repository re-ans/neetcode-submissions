# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        # we have length
        remove_index = length - n
        count = 0

        if remove_index == 0:
            return head.next

        current = head
        for _ in range(remove_index - 1):
            current = current.next

        current.next = current.next.next

        return head