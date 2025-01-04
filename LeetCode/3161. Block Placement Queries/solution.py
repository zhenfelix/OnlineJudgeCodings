from sortedcontainers import SortedList

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        m = max(q[1] for q in queries) + 1
        t = [0] * (2 << m.bit_length())

        # 把 i 处的值改成 val
        def update(o: int, l: int, r: int, i: int, val: int) -> None:
            if l == r:
                t[o] = val
                return
            m = (l + r) // 2
            if i <= m:
                update(o * 2, l, m, i, val)
            else:
                update(o * 2 + 1, m + 1, r, i, val)
            t[o] = max(t[o * 2], t[o * 2 + 1])

        # 查询 [0,R] 中的最大值
        def query(o: int, l: int, r: int, R: int) -> int:
            if r <= R:
                return t[o]
            m = (l + r) // 2
            if R <= m:
                return query(o * 2, l, m, R)
            return max(t[o * 2], query(o * 2 + 1, m + 1, r, R))

        sl = SortedList([0, m])  # 哨兵
        ans = []
        for q in queries:
            x = q[1]
            i = sl.bisect_left(x)
            pre = sl[i - 1]  # x 左侧最近障碍物的位置
            if q[0] == 1:
                nxt = sl[i]  # x 右侧最近障碍物的位置
                sl.add(x)
                update(1, 0, m, x, x - pre)    # 更新 d[x] = x - pre
                update(1, 0, m, nxt, nxt - x)  # 更新 d[nxt] = nxt - x
            else:
                # 最大长度要么是 [0,pre] 中的最大 d，要么是 [pre,x] 这一段的长度
                max_gap = max(query(1, 0, m, pre), x - pre)
                ans.append(max_gap >= q[2])
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/block-placement-queries/solutions/2790395/ping-heng-shu-xian-duan-shu-pythonjavacg-8klz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



from sortedcontainers import *
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        ps = [0,inf]
        for q in queries:
            if q[0] == 1:
                ps.append(q[1])
        ps.sort()
        n = len(ps)
        mp = {v: i for i, v in enumerate(ps)}
        pre = 0
        mx = []
        for p in ps:
            mx.append(p-pre)
            pre = p  
        tree = [0]*n
        def update(pos, x):
            while pos < n:
                tree[pos] = max(tree[pos],x)
                pos += pos&-pos
        def get(pos):
            tmp = 0
            while pos:
                tmp = max(tmp,tree[pos])
                pos -= pos&-pos
            return tmp 
        sl = SortedList(ps)
        for i in range(1,n):
            update(i,mx[i])
        ans = []
        for q in queries[::-1]:
            if q[0] == 1:
                p = q[1]
                sl.remove(p)
                i = sl.bisect_right(p)
                d = sl[i]-sl[i-1]
                update(mp[sl[i]],d)
            else:
                _, p, sz = q 
                i = sl.bisect_right(p)-1
                # print(sl,i)
                if p-sl[i] >= sz: 
                    ans.append(True)
                    continue
                tmp = get(mp[sl[i]])
                if tmp >= sz:
                    ans.append(True)
                else:
                    ans.append(False)
        return ans[::-1]
