class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            
            # the min number is between mid and r
            if nums[mid] > nums[r]:
                l = mid + 1
            # min number could be mid or anywhere between it
            elif nums[mid] < nums[r]:
                r = mid
            else:
                return nums[mid]
        
        return -1