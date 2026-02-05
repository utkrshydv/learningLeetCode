class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isalphanum(s[l]):
                l += 1
            while r > l and not self.isalphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True


    def isalphanum(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))













        # new_str = ""
        # for ch in s:
        #     if ch.isalnum():
        #         new_str += ch.lower()
        # return new_str == new_str[::-1]
        