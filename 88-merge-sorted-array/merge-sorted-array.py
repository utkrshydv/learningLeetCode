class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr = []

        i, j = 0, 0

        while i < m  and j < n:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                arr.append(nums2[j])
                j += 1
            else:
                arr.append(nums1[i])
                arr.append(nums2[j])
                j += 1
                i += 1

        while i < m:
            arr.append(nums1[i])
            i +=1

        while j < n:
            arr.append(nums2[j])
            j+=1

        nums1[:] = arr

        return nums1      