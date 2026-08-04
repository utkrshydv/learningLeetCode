class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        rangemax = max(nums)
        rangemin = min(nums)
        miss_num = []

        for i in range(rangemin, rangemax):
            if i not in nums:
                miss_num.append(i)
        
        return miss_num
        