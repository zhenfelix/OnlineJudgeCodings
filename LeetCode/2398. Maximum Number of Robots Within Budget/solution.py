class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        q = deque()
        j = 0
        ans = 0
        s = 0
        for i in range(n):
            s += runningCosts[i]
            while q and chargeTimes[q[-1]] <= chargeTimes[i]:
                q.pop()
            q.append(i)
            while q and chargeTimes[q[0]]+(i-j+1)*s > budget:
                if q[0] == j:
                    q.popleft()
                s -= runningCosts[j]
                j += 1
            ans = max(ans, i-j+1)
        return ans



class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        def check(k):
            q = deque()
            s = 0
            for i in range(n):
                while q and chargeTimes[q[-1]] <= chargeTimes[i]:
                    q.pop()
                q.append(i)
                s += runningCosts[i]
                if q[0] <= i-k:
                    q.popleft()
                if i >= k:
                    s -= runningCosts[i-k]
                if i >= k-1 and k*s+chargeTimes[q[0]] <= budget:
                    return True
            return False

        lo, hi = 1, n 
        while lo <= hi:
            mid = (lo+hi)//2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
