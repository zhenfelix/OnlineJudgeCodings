class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = spaces[::-1]
        res = []
        tmp = []
        s += "$"
        for i, ch in enumerate(s):
            if i == len(s)-1 or (spaces and i == spaces[-1]):
                if spaces:
                    spaces.pop()
                res.append(''.join(tmp))
                tmp = []
            tmp.append(ch)
        # print(res)
        return ' '.join(res)


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s += "$"
        spaces = [0]+spaces+[len(s)-1]
        t = ' '.join(s[i:j] for i, j in zip(spaces[:-1], spaces[1:]))
        return t


# 作者：吴自华
# 链接：https://leetcode-cn.com/circle/discuss/s1k590/view/l1QubD/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。