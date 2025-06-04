class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> countS = new HashMap<>();
        Map<Character, Integer> countT = new HashMap<>();

        for (char ch : s.toCharArray()){
            countS.put(ch, countS.getOrDefault(ch, 0) + 1);
        }

        for (char ch : t.toCharArray()){
            countT.put(ch, countT.getOrDefault(ch, 0) + 1);
        }
        return countS.equals(countT);
    }
}