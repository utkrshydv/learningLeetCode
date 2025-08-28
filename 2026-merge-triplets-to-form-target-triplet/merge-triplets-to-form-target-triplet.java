class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        int[] check = new int[3];
        int t1 = target[0];
        int t2 = target[1];
        int t3 = target[2];

        for(int[] triplet : triplets){
            int u = triplet[0];
            int v = triplet[1];
            int w = triplet[2];

            if( u>t1 || v>t2 || w > t3){
                continue;
            }
            
            if(u==t1) check[0] = 1;
            if(v==t2) check[1] = 1;
            if(w==t3) check[2] = 1;
        }
        return (check[0] + check[1] + check[2]) == 3;
    }
}