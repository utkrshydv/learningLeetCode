class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charArray = [0]*26
        res = 0

        for char in chars:
            charArray[ord(char) - ord("a")] += 1
        
        for word in words:
            wordArray = [0]*26

            for char in word:
                wordArray[ord(char) - ord("a")] += 1

            possible = True

            for i in range(26):
                if wordArray[i] > charArray[i]:
                    possible = False
                    break
                    
            if possible:
                res += len(word)

        return res


        