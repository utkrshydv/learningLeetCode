class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)

        return nums


        # ans_arr = []

        # for num in nums:
        #     ans_arr.append(num)

        # for num in nums:
        #     ans_arr.append(num)

        # return ans_arr
        