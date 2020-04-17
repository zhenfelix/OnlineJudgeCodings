class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour += minutes/60
        hour = hour*360/12
        minutes = minutes*360/60
        angle = abs(hour-minutes)
        return min(angle,360-angle)