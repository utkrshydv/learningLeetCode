# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return

        ptr1, ptr2 = head, head

        while ptr2.next:
            if ptr2.next.val == ptr1.val:
                ptr2 = ptr2.next
            else:
                ptr1.next = ptr2.next
                ptr1 = ptr2.next
                ptr2 = ptr2.next

        ptr1.next = None

        return head