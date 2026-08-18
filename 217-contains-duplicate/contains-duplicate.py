class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for value in count.values():
            if value > 1:
                return True

        return False
        