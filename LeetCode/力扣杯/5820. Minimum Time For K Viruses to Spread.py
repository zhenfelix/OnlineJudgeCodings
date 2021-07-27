class Solution:
    def minDayskVariants(self, points: List[List[int]], k: int) -> int:
        def dis(x, y):
            return sorted(abs(x - ox) + abs(y - oy) for ox, oy in points)[k-1]
        def cal(x, y):
            step = 10 ** 9
            while step > 1e-1:
                for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    nx, ny = int(x + step * dx), int(y + step * dy)
                    if dis(nx, ny) < dis(x, y):
                        x, y = nx, ny
                    step *= 0.9
            return dis(x, y)
        return min(cal(randint(0, 10**9), randint(0, 10**9)) for _ in range(10))


# 作者：qqwqert007
# 链接：https://leetcode-cn.com/problems/minimum-time-for-k-viruses-to-spread/solution/mo-ni-tui-huo-by-qqwqert007-d07f/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。