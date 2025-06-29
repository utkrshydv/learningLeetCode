class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {

        //brute force
        int[] arr = new int[nums1.length];

        for(int i = 0; i < nums1.length; i++){
            int val = nums1[i];
            boolean found = false;
            int res = -1;

            for(int j = 0; j < nums2.length; j++){
                if(nums2[j] == val){
                    for(int k = j+1; k < nums2.length; k++){
                        if(nums2[k] > val){
                            res = nums2[k];
                            break;
                        }
                    }
                    break;
                }
            }
            arr[i] = res;
        }
        return arr;
    }
}