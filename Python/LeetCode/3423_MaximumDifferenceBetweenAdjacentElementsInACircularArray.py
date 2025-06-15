class MaximumDifferenceBetweenAdjacentElementsInACircularArray:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        if nums is None:
            return 0

        max_adj_dis: int = 0

        for i in range(len(nums)):
            cur_adj_dis: int = abs(nums[i] - nums[(i + 1) % len(nums)])
            max_adj_dis = cur_adj_dis if cur_adj_dis > max_adj_dis else max_adj_dis

        return max_adj_dis
