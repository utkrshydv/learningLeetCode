# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # arr = []

        # temp = head
        # while temp:
        #     arr.append(temp.val)
        #     temp = temp.next

        # return arr == arr[::-1]

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        left, right = head, prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True


        
        