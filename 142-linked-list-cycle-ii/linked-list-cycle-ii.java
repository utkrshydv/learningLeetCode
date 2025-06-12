/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {

        if(head == null){
            return null;
        }

        ListNode slow = head;
        ListNode fast = head;
        int length = 0;

        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;

            if(slow == fast){
                ListNode temp = slow;
               do{
                temp = temp.next;
                length++;
               } while ( temp != slow);
               break;
            }
        }
        if(length == 0){
            return null;
        }

        slow = head;
        fast = head;

        while (length > 0){
            slow = slow.next;
            length--;
        }

        while(slow!=fast){
            slow = slow.next;
            fast = fast.next;
        }

        return slow;

    }
}