class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_seen = set()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_seen:
                return [nums.index(complement), i]
            num_seen.add(nums[i])
        return [0, 0]