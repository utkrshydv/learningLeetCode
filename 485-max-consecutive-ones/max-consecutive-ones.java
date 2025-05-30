class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cunt = 0;
        int maxCunt = 0;

        for(int i = 0; i<nums.length; i++){
          if(nums[i] != 1){
            maxCunt = maxCunt > cunt ? maxCunt : cunt;
            cunt = 0;
          } else {
            cunt++;
          }        
        }

        maxCunt = maxCunt > cunt ? maxCunt : cunt;

        return maxCunt;
    }
}