class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        # stack of arrays [[], [], []]
        fleets = 0
        ahead_time = 0

        for pos, sp in cars:
            time = (target - pos) / sp

            # slower than the previous fleet
            if time > ahead_time:
                fleets += 1
                ahead_time = time

        return fleets

