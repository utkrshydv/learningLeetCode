class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if(words.length != pattern.length()){
            return false;
        }
        HashMap<Character, String> hm = new HashMap<>();
        HashSet<String> usedWords = new HashSet<>();

        for(int i =0; i< pattern.length(); i++){
            char ch = pattern.charAt(i);
            String word = words[i];

            if(hm.containsKey(ch)){
                if(!hm.get(ch).equals(word)){
                    return false;
                }
            } else {
                if(usedWords.contains(word)){
                    return false;
                }
                hm.put(ch, word);
                usedWords.add(word);
            }
        }
       return true;
    }
}