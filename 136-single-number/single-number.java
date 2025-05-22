class Solution {
    public int singleNumber(int[] nums) {
        int expectedNum = nums[0];
        for(int i=1; i<nums.length; i++){
            expectedNum = expectedNum^nums[i];
        }
        return expectedNum;
    }
}