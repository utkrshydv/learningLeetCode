class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        
        Map<Integer, Integer> map = new HashMap<>();
        Stack<Integer> stack = new Stack<>();

        for(int i = nums2.length -1; i >= 0; i--){
            int current = nums2[i];

            while(!stack.isEmpty() && stack.peek() <= current){
                stack.pop();
            }

            map.put(current, stack.isEmpty() ? -1 : stack.peek());

            stack.push(current);
        }

        int[] result = new int[nums1.length];
        for(int i=0; i<nums1.length; i++){
            result[i] = map.get(nums1[i]);
        }

        return result;

       
    }
}

//  //brute force
//         int[] arr = new int[nums1.length];

//         for(int i = 0; i < nums1.length; i++){
//             int val = nums1[i];
//             boolean found = false;
//             int res = -1;

//             for(int j = 0; j < nums2.length; j++){
//                 if(nums2[j] == val){
//                     for(int k = j+1; k < nums2.length; k++){
//                         if(nums2[k] > val){
//                             res = nums2[k];
//                             break;
//                         }
//                     }
//                     break;
//                 }
//             }
//             arr[i] = res;
//         }
//         return arr;