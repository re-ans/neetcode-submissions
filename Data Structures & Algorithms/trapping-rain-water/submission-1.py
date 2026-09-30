class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        
        maxLeft[0] = height[0]
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i])

        maxRight[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(height[i], maxRight[i + 1])
        
        res = 0

        for i in range(len(height)):
            res += min(maxLeft[i], maxRight[i]) - height[i]

        return res