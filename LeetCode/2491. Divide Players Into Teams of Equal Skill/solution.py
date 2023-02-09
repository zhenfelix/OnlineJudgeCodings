class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans, s = 0, skill[0] + skill[-1]
        for i in range(len(skill) // 2):
            x, y = skill[i], skill[-1 - i]
            if x + y != s: return -1
            ans += x * y
        return ans


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/T0eOvC/view/WCSm5y/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)//2
        s = sum(x for x in skill)
        if s%n != 0:
            return -1
        s //= n 
        if any(x >= s for x in skill):
            return -1
        # print(s)
        cc = Counter(skill)
        ans = 0 
        lo, hi = 1, s-1 
        while lo < hi:
            if cc[lo] != cc[hi]:
                return -1
            ans += (lo*hi)*cc[lo]
            lo += 1
            hi -= 1
        if lo == hi:
            ans += lo*hi*cc[lo]//2
        return ans 