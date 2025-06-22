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
    public ListNode reverseKGroup(ListNode head, int k) {

        int count = 0;
        ListNode temp = head;

        while(temp!=null && count<k){
            temp = temp.next;
            count++;
        }

        if(count < k) return head;

        ListNode prev = null, next = null;
        ListNode current = head;

        for(int i= 0; i< k; i++){
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }

        ListNode newHead = prev;
        head.next = reverseKGroup(temp, k);
        return newHead;
        
    }
}