class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left, right = 1, 1

        # for right in range(1, len(nums)):
        #     if nums[right] != nums[right-1]:
        #         nums[left] = nums[right]
        #         left += 1
        # return left

        i = 0
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i+1
        