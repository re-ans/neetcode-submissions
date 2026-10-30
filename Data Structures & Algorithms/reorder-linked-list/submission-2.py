# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # split the list before reversing
        mid = slow.next
        slow.next = None
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        
        # after reversing the half, PREV should be the head of the reversed half?

        first = head
        second = prev
        while first and second:
            # save the next pointers
            next_first = first.next
            next_second = second.next

            # first -> second -> first.next -> second.next
            # these are now overwritten
            first.next = second
            second.next = next_first

            first = next_first
            second = next_second

        # return first
        