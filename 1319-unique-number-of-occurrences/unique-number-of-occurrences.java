class Solution {
    public boolean uniqueOccurrences(int[] arr) {
     int[] freq = new int[2001];

     for(int num : arr){
        freq[num+1000]++;
     }

     Set<Integer> seen = new HashSet<>();

     for(int count : freq){
        if(count > 0){
            if(seen.contains(count)){
                return false;
            }
            seen.add(count);
        }
     }
     return true;
    }
}