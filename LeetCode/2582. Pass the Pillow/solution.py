class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time = time%((n-1)*2)
        if time <= n-1:
            return time+1
        else:
            return (n-1)*2-time+1