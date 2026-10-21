class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack = []
        # stack = [30]
        res = [0] * len(temperatures)
        stack = [] # temp, index

        for i, t in enumerate(temperatures):
            # curr temp is warmer than last temp on stack
            while stack and t > stack[-1][0]:
                stack_temp, stack_i = stack.pop()
                res[stack_i] = i - stack_i
            stack.append((t, i))

        return res