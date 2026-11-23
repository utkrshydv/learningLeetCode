class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for char in s:
            if char.isalnum():
                t += char

        for i in range(len(t)):
            if t[i].lower() != t[len(t)-1- i].lower():
                return False

        return True
        