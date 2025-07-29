class Solution {
    public int missingNumber(int[] nums) {

        int arrXor = nums[0];

        for(int i = 1; i < nums.length; i++){
            arrXor = arrXor^nums[i];
        }

        for(int j = 0; j<=nums.length; j++){
            arrXor = arrXor^j;
        }

        return arrXor;
        
    }
}