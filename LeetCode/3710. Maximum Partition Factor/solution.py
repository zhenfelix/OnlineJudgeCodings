class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        if len(points) == 2:
            return 0

        # 原理见 785. 判断二分图
        def check(low: int) -> bool:
            colors = [0] * len(points)

            def dfs(x: int, c: int) -> bool:
                colors[x] = c
                x1, y1 = points[x]
                for y, (x2, y2) in enumerate(points):
                    if y == x or abs(x1 - x2) + abs(y1 - y2) >= low:  # 符合要求
                        continue
                    if colors[y] == c or colors[y] == 0 and not dfs(y, -c):
                        return False  # 不是二分图
                return True

            # 可能有多个连通块
            for i, c in enumerate(colors):
                if c == 0 and not dfs(i, 1):
                    return False
            return True

        max_dis = max(abs(x1 - x2) + abs(y1 - y2)
                      for (x1, y1), (x2, y2) in combinations(points, 2))

        left, right = 0, max_dis + 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid+1
            else:
                right = mid-1
        return right

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-partition-factor/solutions/3803673/er-fen-da-an-pan-duan-er-fen-tu-pythonja-56r2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。