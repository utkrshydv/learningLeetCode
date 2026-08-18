from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = len(nums)//2

        freq = Counter(nums)
        for key, value in freq.items():
            if value > limit:
                return key

        