class Solution {
    public int minimumCost(int[] cost) {
        Arrays.sort(cost);
        int result = 0;
        int n = cost.length;

        for(int i =0; i < n; i++){
            if(i%3 != n%3){
                result += cost[i];
            }
        }
        return result;
    }
}