class Solution {
    public int missingNumber(int[] nums) {
        int num = nums[0];

        for(int i =1; i <nums.length; i++){
            num = num^nums[i];
        }

        for(int j = 0; j <= nums.length; j++){
            num = num^j;
        }

        return num;
    }
}