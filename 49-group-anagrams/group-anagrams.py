class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0]*26

            for character in word:
                count[ord(character) - ord("a")] += 1

            res[tuple(count)].append(word)

        return list(res.values())

        






        #res = {}
        # for word in strs:
        #     sorted_word = "".join(sorted(word))

        #     if sorted_word not in res:
        #         res[sorted_word] = []
            
        #     res[sorted_word].append(word)

        # return list(res.values())


        