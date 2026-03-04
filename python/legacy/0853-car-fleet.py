from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        leader = None
        fleets = 0

        for p, s in cars:
            time = (target-p) / s
            if not leader or time > leader:
                fleets += 1
                leader = time
        
        return fleets