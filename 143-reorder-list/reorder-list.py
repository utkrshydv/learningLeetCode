# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = self.rev(slow.next)
        slow.next = None
        
        first = head

        while head2:
            temp1 = first.next
            temp2 = head2.next

            first.next = head2
            head2.next = temp1

            first = temp1
            head2 = temp2



    def rev(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev

        