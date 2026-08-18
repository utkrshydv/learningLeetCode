from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        sorted_freq = sorted(freq.items(), key = lambda x:x[1], reverse=True)

        new_s = ""

        for x, y in sorted_freq:
            new_s += x*y

        return new_s
