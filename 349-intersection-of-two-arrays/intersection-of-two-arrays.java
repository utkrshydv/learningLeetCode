import java.util.Arrays;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);

        int[] array = new int[Math.min(nums1.length, nums2.length)];
        int i = 0, j = 0, k = 0;

        while(i<nums1.length && j<nums2.length){
            if(nums1[i] < nums2[j]){
                i++;
            } else if(nums1[i] > nums2[j]){
                j++;
            } else{
                if(k==0 || array[k-1] != nums1[i]){
                    array[k++] = nums1[i];
                }
                i++;
                j++;
            }
        }
        return Arrays.copyOfRange(array, 0, k);

    }
}
