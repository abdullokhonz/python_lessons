class TwoSum:
    def twoSum(self, nums, target):
        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

        return []

two_sum = TwoSum()
result = two_sum.twoSum([2, 7, 11, 15], 9)
print(result)
