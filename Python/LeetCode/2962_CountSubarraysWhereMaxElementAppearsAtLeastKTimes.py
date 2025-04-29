class CountSubarraysWhereMaxElementAppearsAtLeastKTimes:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        max_num: int = max(nums)
        result, left, count = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == max_num:
                count += 1

            while count >= k:
                result += len(nums) - right

                if nums[left] == max_num:
                    count -= 1
                left += 1

        return result
