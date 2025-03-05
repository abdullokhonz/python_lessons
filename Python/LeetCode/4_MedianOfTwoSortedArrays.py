class MedianOfTwoSortedArrays:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums: list[int] = [0] * (len(nums1) + len(nums2))

        i, j, k = 0, 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1
            k += 1

        while i < len(nums1):
            nums[k] = nums1[i]
            i += 1
            k += 1

        while j < len(nums2):
            nums[k] = nums2[j]
            j += 1
            k += 1

        length = len(nums)

        if length % 2 == 0:
            result = (nums[length // 2 - 1] + nums[length // 2]) / 2.0
        else:
            result = nums[length // 2]

        return result
