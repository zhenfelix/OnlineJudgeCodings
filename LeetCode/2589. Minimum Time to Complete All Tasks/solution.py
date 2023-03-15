# lcp32

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        mx = max([b for a,b,c in tasks])
        intervals = [0]*(mx+5)
        tasks.sort(key = lambda x: x[1])
        for a, b, c in tasks:
            cnt = sum(intervals[a:b+1])
            if cnt >= c: continue
            cnt = c-cnt
            for p in range(a,b+1)[::-1]:
                if intervals[p] == 0:
                    intervals[p] = 1
                    cnt -= 1
                if cnt <= 0: break
        return sum(intervals)

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        mx = max([b for a,b,c in tasks])
        st = []
        cur = 0
        tasks.sort(key = lambda x: x[1])
        for a, b, c in tasks:
            while cur <= b:
                st.append(cur)
                cur += 1
            idx = bisect_left(st, a)
            r = c-(b-a+1-len(st)+idx)
            while r > 0:
                st.pop()
                r -= 1
        return cur-len(st)


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.append([10**9+1, 10**9+1, 1]) #加个哨兵
        res, q = 0, []
        for [s, e, p] in sorted(tasks, key=lambda x:x[0]) :
            while q and q[0][0]+res < s :
                if q[0][0]+res >= q[0][1]: heapq.heappop(q) #任务早已完成，移除
                else : res += min(q[0][1], s) - (q[0][0]+res)
            heapq.heappush(q, [e-p+1-res, e+1])
        return res

# 作者：Foxtail
# 链接：https://leetcode.cn/problems/t3fKg1/solutions/706785/10xing-jie-jue-zhan-dou-by-foxtail-ke2e/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。