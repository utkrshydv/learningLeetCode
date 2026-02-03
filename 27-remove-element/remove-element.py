class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

        # res = []

        # for num in nums:
        #     if num != val:
        #         res.append(num)

        # for i in range(len(res)):
        #     nums[i] = res[i]

        # return len(res)
            