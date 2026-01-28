class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow




        
        
        
        
        
        
        
        
        
        
        
        # should not have been accepted. 
        
        # freq = defaultdict(int)

        # for num in nums:
        #     freq[num] += 1

        # for k, v in freq.items():
        #     if v > 1:
        #         return k
        