class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        main_set = set()

        for num in nums:
            if num in main_set:
                return True
            else:
                main_set.add(num)

        
        return False
        