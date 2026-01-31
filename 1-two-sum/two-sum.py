class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in prev:
                return [prev[diff], index]
            prev[num] = index

        return
        