class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        for k, v in freq.items():
            if v > 1:
                return k
        