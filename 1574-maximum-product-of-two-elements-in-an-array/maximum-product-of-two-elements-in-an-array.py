class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr = nums[0]

        result = 0

        for i in range(1, len(nums)):
            result = max(result, (nums[i]-1) * (curr - 1))
            curr = max(curr, nums[i])


        return result
        