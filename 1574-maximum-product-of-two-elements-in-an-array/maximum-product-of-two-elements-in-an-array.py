class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # curr = nums[0]

        # result = 0

        # for i in range(1, len(nums)):
        #     result = max(result, (nums[i]-1) * (curr - 1))
        #     curr = max(curr, nums[i])


        # return result

        # Approach 2

        largest, second_largest = 0, 0

        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            else:
                second_largest = max(second_largest, num)
            
        return (largest - 1) * (second_largest - 1)
        