class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int l = 0;
        int size = arr.length - 1;
        while (l < size){
            int mid = l + (size - l)/2;
            if(arr[mid] < arr[mid+1]){
                l = mid+1;
            } else {
                size = mid;
            }
        }
        return l;
    }
}