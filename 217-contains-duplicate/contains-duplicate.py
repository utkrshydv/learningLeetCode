from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frq = Counter(nums)
    
        for count in frq.values():
            if count > 1: return True

        return False
            