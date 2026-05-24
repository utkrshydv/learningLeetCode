from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        n = len(s)

        if max(freq.values())>(n+1)//2:
            return ""

        res = [""]*n

        chars = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        index = 0

        for char in chars:
            while freq[char] > 0:
                if index >=n:
                    index = 1

                res[index] = char
                index += 2
                freq[char] -= 1

        return "".join(res)
        