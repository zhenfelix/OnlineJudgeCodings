class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        arr = []
        n = len(releaseTimes)
        for i in range(n):
            if i > 0:
                arr.append((releaseTimes[i]-releaseTimes[i-1], keysPressed[i]))
            else:
                arr.append((releaseTimes[i],keysPressed[i]))
        arr.sort()
        # print(arr)
        return arr[-1][-1]