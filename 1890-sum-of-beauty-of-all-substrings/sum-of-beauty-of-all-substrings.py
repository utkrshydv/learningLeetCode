class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            freq = {}

            for j in range(i, len(s)):
                char = s[j]

                freq[char] = freq.get(char, 0) + 1
                beauty = max(freq.values()) - min(freq.values())

                total += beauty

        return total
        