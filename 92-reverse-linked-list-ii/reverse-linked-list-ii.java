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

        if(head == null || left == right ) return head;

        ListNode dummyHead = new ListNode();
        dummyHead.next = head;

        ListNode reversePrev = dummyHead;

        for(int i = 0; i < left-1; i++){
            reversePrev = reversePrev.next;
        }

        ListNode prev = null, next = null, current = reversePrev.next;
        ListNode tail = current;

        for(int i = 0; i<right-left+1; i++){
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }

        reversePrev.next = prev;
        tail.next = current;

        return dummyHead.next;

    }
}