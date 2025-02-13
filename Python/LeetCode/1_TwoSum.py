class TwoSum:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict: dict = {}

        for i, num in enumerate(nums):
            complement: int = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

        return []

two_sum = TwoSum()
result = two_sum.twoSum([2, 7, 11, 15], 9)
print(result)
