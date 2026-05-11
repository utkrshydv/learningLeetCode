class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = {}
        for letter in stones:
            freq[letter] = freq.get(letter, 0) + 1

        count = 0

        for jewel in jewels:
            count = count + freq.get(jewel, 0)

        return count 
        