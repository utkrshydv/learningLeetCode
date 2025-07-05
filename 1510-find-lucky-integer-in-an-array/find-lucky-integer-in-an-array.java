class Solution {
    public int findLucky(int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int element : arr){
            map.put(element, map.getOrDefault(element, 0) + 1);
        }

        int max = 0;

        for(Map.Entry<Integer, Integer> element : map.entrySet()){
            if(element.getKey() == element.getValue()){
                max = Math.max(max, element.getKey());
            }
        }

        return max == 0 ? -1 : max;
    }
}