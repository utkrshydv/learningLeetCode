class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i = 1
        while True:
            
            num = k
            num = num*i
            i+=1
            if num in nums:
                continue
            else:
                return num



        