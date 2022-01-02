class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        for cur in sorted(asteroids):
            if mass < cur:
                return False
            mass += cur
        return True