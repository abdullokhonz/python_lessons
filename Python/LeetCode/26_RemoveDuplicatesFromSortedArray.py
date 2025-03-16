class RemoveDuplicatesFromSortedArray:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        index: int = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1

        return index
