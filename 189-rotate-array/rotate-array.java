class Solution {
    public void rotate(int[] nums, int k) {
        int size = nums.length;
        int d = k % size;

        if(d == 0) return;

        reverse(nums, 0, size-1);
        reverse(nums, 0, d-1);
        reverse(nums, d, size-1);
       
    }

    public static void reverse(int[] array, int start, int end){
        while(start<end){
            int temp = array[start];
            array[start] = array[end];
            array[end] = temp;
            end--;
            start++;
        }
    }

}