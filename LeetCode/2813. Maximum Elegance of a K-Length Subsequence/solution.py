class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda i: -i[0])  # 把利润从大到小排序
        ans = total_profit = 0
        vis = set()
        duplicate = []  # 最小堆
        for i, (profit, category) in enumerate(items):
            if i < k:
                total_profit += profit
                if category not in vis:
                    vis.add(category)
                else:  # 重复类别
                    heappush(duplicate, profit)
            elif category not in vis and duplicate:
                vis.add(category)
                total_profit += profit - heappop(duplicate)  # 选一个重复类别中的最小利润替换
            # else: 比前面的利润小，而且类别还重复了，选它只会让 total_profit 变小，len(vis) 不变，优雅度不会变大
            ans = max(ans, total_profit + len(vis) * len(vis))
        return ans


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/chtVBq/view/jLRq1W/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        n = len(items)
        items.sort(key = lambda x: -x[0])
        cc = Counter()
        s = 0
        ans = 0
        for v, t in items[:k]:
            cc[t] += 1
            s += v 
        ans = s+len(cc)**2
        hq = []
        for v, t in items[:k]:
            if cc[t] > 1:
                hq.append((v,t))
        heapify(hq)
        for v, t in items[k:]:
            if cc[t] > 0:
                continue
            while hq and cc[hq[0][1]] == 1:
                heappop(hq)
            if hq:
                v_, t_ = heappop(hq)
                cc[t_] -= 1
                cc[t] += 1
                s -= v_
                s += v 
                ans = max(ans, s+len(cc)**2)
        return ans 


