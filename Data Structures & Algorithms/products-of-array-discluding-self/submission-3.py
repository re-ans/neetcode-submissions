class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = suffix[n - 1] = 1 # set first of prefix to 1 and last of suffix to 1
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res