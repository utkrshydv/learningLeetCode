class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        sorted_map = [k for k,v in sorted(hashmap.items(), key = lambda item : item[1], reverse  = True)]


        return sorted_map[:k]

                