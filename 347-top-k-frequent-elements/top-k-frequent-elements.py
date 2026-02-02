class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

            # res = []
            # hashmap = {}

            # for num in nums:
            #     hashmap[num] = 1 + hashmap.get(num, 0)

            # sorted_map = [k for k,v in sorted(hashmap.items(), key = lambda item : item[1], reverse  = True)]

            # return sorted_map[:k]


#             Approach	Time Complexity
#             Sorting-based	O(n log n)
#             Bucket-based	O(n)
