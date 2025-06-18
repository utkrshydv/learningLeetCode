/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
      if(head == null || head.next == null) return true;

      ListNode slow =  head, fast = head;
      
      while(fast != null && fast.next != null){
        fast = fast.next.next;
        slow = slow.next;
      }

      ListNode firstHalf = head;
      ListNode secondHalf = reverse(slow);

      while(secondHalf != null){
        if(firstHalf.val != secondHalf.val){
            return false;
        }
        firstHalf = firstHalf.next;
        secondHalf = secondHalf.next;
      }
     return true;
    }

    ListNode reverse(ListNode head){
        if(head == null || head.next == null) return head;

        ListNode reversedHead = reverse(head.next);

        head.next.next = head;
        head.next = null;

        return reversedHead;
    }
}