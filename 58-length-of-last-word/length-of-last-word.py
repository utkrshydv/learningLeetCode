class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_arr = s.split()
        return len(str_arr[-1])
        