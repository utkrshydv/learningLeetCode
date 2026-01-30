class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_arr = [0]*26

        for c in s:
            char_arr[ord(c) - ord("a")] += 1
        
        for i, c in enumerate(s):
            if char_arr[ord(c) - ord("a")] == 1:
                return i
            
        
        return -1
        