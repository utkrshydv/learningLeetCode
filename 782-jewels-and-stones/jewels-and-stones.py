class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # freq = {}
        # for letter in stones:
        #     freq[letter] = freq.get(letter, 0) + 1

        # count = 0

        # for jewel in jewels:
        #     count = count + freq.get(jewel, 0)

        # return count 
        jewel_set = set(jewels)

        count = 0

        for stone in stones:
            if stone in jewel_set:
                count += 1

        return count