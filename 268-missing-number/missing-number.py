class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n+1))//2

        sum = 0

        for i in range(len(nums)):
            sum += nums[i] 
        
        return expected_sum - sum