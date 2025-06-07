class Solution {
    public int lengthOfLongestSubstring(String s) {
     List<Character> window = new ArrayList<>(); 
     int maxLength = 0;

     for(int i =0; i<s.length(); i++){
        char c = s.charAt(i);

        while(window.contains(c)){
            window.remove(0);
        }

        window.add(c);

        if(window.size() > maxLength){
            maxLength = window.size();
        }
     }
     return maxLength;
    }
}