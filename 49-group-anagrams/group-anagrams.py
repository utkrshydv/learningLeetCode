class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in res:
                res[sorted_word] = []
            
            res[sorted_word].append(word)

        return list(res.values())


        