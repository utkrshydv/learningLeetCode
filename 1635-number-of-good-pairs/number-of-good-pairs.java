class Solution {
    public int numIdenticalPairs(int[] nums) {

        Map<Integer, Integer> map = new HashMap<>();

        for(int num : nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        int count = 0;

        for(int val : map.values()){
            if(val > 1){
                count += (val*(val-1))/2;
            }
        }
       
        
        return count;
    }
}