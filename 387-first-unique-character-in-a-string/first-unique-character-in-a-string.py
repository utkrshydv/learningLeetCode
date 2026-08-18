from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq = Counter(s)
        sorted_freq = sorted(freq.items(), key = lambda x : x[1])
        char_arr = [0]*26

        if sorted_freq[0][1] == 1:
            return s.index(sorted_freq[0][0])
        
        return -1
        