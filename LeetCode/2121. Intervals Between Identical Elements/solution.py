class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        mp = defaultdict(list)
        for i, v in enumerate(arr):
            mp[v].append(i)
        res = [0]*n 
        def dfs(pos):
            left = right = cl = cr = 0
            for i in range(1,len(pos)):
                right += pos[i]-pos[0]
                cr += 1
            res[pos[0]] = right
            for i in range(1,len(pos)):
                delta = pos[i]-pos[i-1]
                right -= delta*cr
                cr -= 1
                cl += 1
                left += delta*cl 
                res[pos[i]] = left+right
            return
        for k, p in mp.items():
            dfs(p)
        return res


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        d = collections.defaultdict(list)
        for i, num in enumerate(arr):
            d[num].append(i)
            
        ans = [0] * len(arr)
        for v in d.values():
            m = len(v)
            cval = sum(v) - v[0] * m
            for i, pos in enumerate(v):
                delta = v[i] - v[i - 1] if i >= 1 else 0
                cval += i * delta - (m - i) * delta
                ans[pos] = cval
            
        return ans


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/NS4Y2j/view/dIMeD8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。