class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxChar = ' '
        for i in range(2, len(num)):
            if num[i] == num[i-1] and num[i] == num[i-2]:
                maxChar = max(maxChar, num[i])

        if maxChar == ' ':
            return  ""

        return maxChar*3

        