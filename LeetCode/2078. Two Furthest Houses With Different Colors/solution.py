class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0
        for i, c in enumerate(colors):
            for j in range(i):
                if colors[j] != colors[i]:
                    res = max(res, i-j)
        return res


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        return max(abs(i - j) for i, ic in enumerate(colors) for j, jc in enumerate(colors) if ic != jc)


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/sfeav2/view/eQBxyC/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        if colors[0] != colors[n - 1]:
            return n - 1
        
        l = 1
        while colors[l] == colors[0]:
            l += 1
        r = n - 2
        while colors[r] == colors[n - 1]:
            r -= 1
        return max(r, n - 1 - l)


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/sfeav2/view/eQBxyC/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。