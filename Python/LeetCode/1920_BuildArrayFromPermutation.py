class BuildArrayFromPermutation:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans: list[int] = [0] * len(nums)

        for i in range(len(nums)):
            ans[i] = nums[nums[i]]

        return ans
