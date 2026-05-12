class Solution:
    def maxFreqSum(self, s: str) -> int:
        v_count = {}
        c_count = {}
        vowels = ['a', 'e', 'i', 'o', 'u']

        for char in s:
            if char in vowels:
                v_count[char] = v_count.get(char, 0) + 1
            else:
                c_count[char] = c_count.get(char, 0) + 1

        count = max(v_count.values(), default=0) + max(c_count.values(), default=0)

        return count
        