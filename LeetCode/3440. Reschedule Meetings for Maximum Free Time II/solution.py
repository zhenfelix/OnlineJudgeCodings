class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        def get(i: int) -> int:
            if i == 0:
                return startTime[0]
            if i == n:
                return eventTime - endTime[n - 1]
            return startTime[i] - endTime[i - 1]

        a, b, c = 0, -1, -1
        for i in range(1, n + 1):
            sz = get(i)
            if sz > get(a):
                a, b, c = i, a, b
            elif b < 0 or sz > get(b):
                b, c = i, b
            elif c < 0 or sz > get(c):
                c = i

        ans = 0
        for i, (s, e) in enumerate(zip(startTime, endTime)):
            sz = e - s
            if i != a and i + 1 != a and sz <= get(a) or \
               i != b and i + 1 != b and sz <= get(b) or \
               sz <= get(c):
                ans = max(ans, get(i) + sz + get(i + 1))
            else:
                ans = max(ans, get(i) + get(i + 1))
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-ii/solutions/3061629/wei-hu-qian-san-da-de-kong-wei-mei-ju-fe-xm2f/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。