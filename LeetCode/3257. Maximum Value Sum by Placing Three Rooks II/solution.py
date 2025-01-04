class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        def update(row: List[int]) -> None:
            for j, x in enumerate(row):
                for k in range(3):
                    if x > p[k][0] and all(j != j2 for _, j2 in p[:k]):
                        p[k], (x, j) = (x, j), p[k]

        m = len(board)
        suf = [None] * m
        p = [(-inf, -1)] * 3  # 最大、次大、第三大
        for i in range(m - 1, 1, -1):
            update(board[i])
            suf[i] = p[:]

        ans = -inf
        p = [(-inf, -1)] * 3  # 重置，计算 pre
        for i, row in enumerate(board[:-2]):
            update(row)
            for j2, y in enumerate(board[i + 1]):  # 第二个车
                for x, j1 in p:  # 第一个车
                    for z, j3 in suf[i + 2]:  # 第三个车
                        if j1 != j2 and j1 != j3 and j2 != j3:  # 没有同列的车
                            ans = max(ans, x + y + z)  # 注：手动 if 更快
                            break
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-value-sum-by-placing-three-rooks-ii/solutions/2884186/qian-hou-zhui-fen-jie-pythonjavacgo-by-e-gc48/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        def update(row: List[int]) -> None:
            for j, x in enumerate(row):
                flag = True
                for k in range(3):
                    if p[k][-1] == j:
                        flag = False
                        if p[k][0] < x: p[k] = (x,j)
                        break
                if flag:
                    p.append((x,j))
                p.sort(reverse=True)
                if len(p) > 3:
                    p.pop()
                print(p)

        m = len(board)
        suf = [None] * m
        p = [(-inf, -1)] * 3  # 最大、次大、第三大
        for i in range(m - 1, 1, -1):
            update(board[i])
            suf[i] = p[:]

        ans = -inf
        p = [(-inf, -1)] * 3  # 重置，计算 pre
        for i, row in enumerate(board[:-2]):
            update(row)
            for j2, y in enumerate(board[i + 1]):  # 第二个车
                for x, j1 in p:  # 第一个车
                    for z, j3 in suf[i + 2]:  # 第三个车
                        if j1 != j2 and j1 != j3 and j2 != j3:  # 没有同列的车
                            ans = max(ans, x + y + z)  # 注：手动 if 更快
                            break
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-value-sum-by-placing-three-rooks-ii/solutions/2884186/qian-hou-zhui-fen-jie-pythonjavacgo-by-e-gc48/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。