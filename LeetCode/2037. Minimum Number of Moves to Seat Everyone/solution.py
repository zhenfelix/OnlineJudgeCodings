class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        res = 0
        for a, b in zip(sorted(seats), sorted(students)):
            res += abs(a-b)
        return res