class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        m = len(persons)
        ps = list(range(m))
        ps.sort(key = lambda x: persons[x])
        intervals = []
        for s, e in flowers:
            intervals.append((s,1))
            intervals.append((e+1,-1))
        intervals.sort(reverse = True)
        cnt = 0
        ans = [0]*m 
        for p in ps:
            t = persons[p]
            while intervals and intervals[-1][0] <= t:
                tt, delta = intervals.pop()
                cnt += delta
            ans[p] = cnt
        return ans 



class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        starts = sorted(s for s, _ in flowers)
        ends = sorted(e for _, e in flowers)
        return [bisect_right(starts, p) - bisect_left(ends, p) for p in persons]


# 作者：endlesscheng
# 链接：https://leetcode-cn.com/problems/number-of-flowers-in-full-bloom/solution/chai-fen-pythonjavacgo-by-endlesscheng-wz35/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。