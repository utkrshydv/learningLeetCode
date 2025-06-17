class Solution {
    public boolean isSubsequence(String s, String t) {

       char[] strS = s.toCharArray();
       char[] strT = t.toCharArray();

       int i = 0;
       int j = 0;

       while( i< s.length() && j < t.length() ){
        if(strS[i] == strT[j]){
            i++;
        }
        j++;
       }

       return i == strS.length;
    }
}