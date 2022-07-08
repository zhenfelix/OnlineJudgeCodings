class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        n, m = len(s), len(sub)
        cc = defaultdict(set)
        for a, b in mappings:
            cc[a].add(b)
        for ch in sub:
            cc[ch].add(ch)
        for i in range(n-m+1):
            flag = True
            for j in range(m):
                if s[i+j] not in cc[sub[j]]:
                    # print(i,j,s[i+j],sub[j])
                    flag = False
                    break
            if flag:
                return True
        return False


class Solution:
    def matchReplacement(self, s: str, sub: str, m: List[List[str]]) -> bool:
        d = defaultdict(set)
        for i, j in m:
            d[i].add(j)
        for i in range(len(s) - len(sub) + 1):
            for j in range(len(sub)):
                if s[i + j] != sub[j] and s[i + j] not in d[sub[j]]:
                    break
            else:
                return True
        return False


作者：caidd
链接：https://leetcode.cn/circle/discuss/zEDpCN/view/0TsH9Q/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。