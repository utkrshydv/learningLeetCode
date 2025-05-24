class Solution {
    public int thirdMax(int[] nums) {
        long first = Long.MIN_VALUE;
        long second = Long.MIN_VALUE;
        long third = Long.MIN_VALUE;
        boolean foundThird = false;  

        for (int num : nums) {
            long n = (long) num;  
            if (n == first || n == second || n == third) {
                continue;
            }
            
            if (n > first) {
                third = second;
                second = first;
                first = n;
                foundThird = true;
            } else if (n > second) {
                third = second;
                second = n;
                foundThird = true;
            } else if (n > third) {
                third = n;
                foundThird = true;
            }
        }
        
        return  third != Long.MIN_VALUE ? (int) third : (int) first;
    }
}
