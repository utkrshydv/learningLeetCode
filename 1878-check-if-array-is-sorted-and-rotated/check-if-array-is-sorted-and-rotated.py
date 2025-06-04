class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(0, len(nums)):
            next = (i+1)%len(nums)
            if nums[i] > nums[next]:
                count +=1
        
        return count <= 1