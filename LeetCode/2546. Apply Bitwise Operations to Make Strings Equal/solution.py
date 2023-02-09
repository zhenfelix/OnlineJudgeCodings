class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        flag = [0]*4
        for a, b in zip(s,target):
            a = int(a)
            b = int(b)
            flag[a|(b<<1)] |= 1
        if flag[3]:
            return True
        return not (flag[1]^flag[2])


class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return ('1' in s) == ('1' in target)


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/circle/discuss/Kclgr5/view/MEVwaD/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。