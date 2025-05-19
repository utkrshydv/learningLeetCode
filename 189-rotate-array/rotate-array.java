class Solution {
    public void rotate(int[] nums, int k) {
        int size = nums.length;
        int d = k%size;

        reverseArray(nums, 0, size-1);
        reverseArray(nums, 0, d-1);
        reverseArray(nums, d, size-1);
    }

    static void reverseArray(int[] array, int start, int end){

        while(start < end){
            int temp = array[start];
            array[start] = array[end];
            array[end] = temp;
            start++;
            end--;
        }
    }
}