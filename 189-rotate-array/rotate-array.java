class Solution {
    public void rotate(int[] nums, int k) {
        int size = nums.length -1;
        int d = k%(size+1);
        if(d==0) return;
        reverse(nums, 0, size);
        reverse(nums, 0, d-1);
        reverse(nums, d, size);
    }

    void reverse(int[] arr, int start, int end){
        while(start < end){
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++; end--;
        }
    }
}