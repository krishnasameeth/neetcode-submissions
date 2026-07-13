# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head):
            curr = head
            prev = None

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        
        dummy = curr = reverse(head)
        if n == 1:
            return reverse(curr.next)
        position = 1

        while position < n - 1 and curr.next:
            curr = curr.next
            position += 1
        
        curr.next = curr.next.next

        return reverse(dummy)