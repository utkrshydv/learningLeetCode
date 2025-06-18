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
    public ListNode reverseBetween(ListNode head, int left, int right) {

        if(head == null || left == right) return head;

        ListNode dummy = new ListNode();
        dummy.next = head;

        ListNode reversePrev = dummy;

        for(int i = 1; i < left; i++){
            reversePrev = reversePrev.next;
        }

        ListNode current = reversePrev.next;
        ListNode tail = current;

        ListNode next = null;
        ListNode prev = null;

        for(int i = 0; i < right-left+1; i++){
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }

        reversePrev.next = prev;
        tail.next = current;

        return dummy.next;

    }
}