class FindSumPairs {

    int[] nums1, nums2;
    Map<Integer, Integer> freq;

    public FindSumPairs(int[] nums1, int[] nums2) {
        this.nums1 = nums1;
        this.nums2 = nums2;
        this.freq = new HashMap<>();
        for(int num : nums2){
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }        
    }
    
    public void add(int index, int val) {

        int oldVal = nums2[index];
        int newVal = oldVal + val;

        freq.put(oldVal, freq.get(oldVal) - 1);
        if(freq.get(oldVal) == 0) freq.remove(oldVal);

        nums2[index] = newVal;
        freq.put(newVal, freq.getOrDefault(newVal, 0) + 1);
    }
    
    public int count(int tot) {
        int count = 0;
        for(int num : nums1){
            int target = tot - num;
            count += freq.getOrDefault(target, 0);
        }
        return count;
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs obj = new FindSumPairs(nums1, nums2);
 * obj.add(index,val);
 * int param_2 = obj.count(tot);
 */