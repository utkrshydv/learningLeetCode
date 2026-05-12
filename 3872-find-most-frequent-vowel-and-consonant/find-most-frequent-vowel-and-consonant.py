class Solution:
    def maxFreqSum(self, s: str) -> int:
        # v_count = {}
        # c_count = {}
        # vowels = ['a', 'e', 'i', 'o', 'u']

        # for char in s:
        #     if char in vowels:
        #         v_count[char] = v_count.get(char, 0) + 1
        #     else:
        #         c_count[char] = c_count.get(char, 0) + 1

        # count = max(v_count.values(), default=0) + max(c_count.values(), default=0)

        # return count

        freq = {}
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        max_v = 0
        max_c = 0

        for char in freq:
            if char in vowels:
                max_v = max(max_v, freq[char])
            else:
                max_c = max(max_c, freq[char])

        return max_v + max_c
        