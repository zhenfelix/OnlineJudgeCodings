class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        p1, p2, p3 = p.split('*')

        # 三段各自在 s 中的所有匹配位置
        pos1 = self.kmp_search(s, p1)
        pos2 = self.kmp_search(s, p2)
        pos3 = self.kmp_search(s, p3)

        ans = inf
        i = k = 0
        # 枚举中间（第二段），维护最近的左右（第一段和第三段）
        for j in pos2:
            # 右边找离 j 最近的子串（但不能重叠）
            while k < len(pos3) and pos3[k] < j + len(p2):
                k += 1
            if k == len(pos3):  # 右边没有
                break
            # 左边找离 j 最近的子串（但不能重叠）
            while i < len(pos1) and pos1[i] <= j - len(p1):
                i += 1
            # 循环结束后，pos1[i-1] 是左边离 j 最近的子串下标（首字母在 s 中的下标）
            if i > 0:
                ans = min(ans, pos3[k] + len(p3) - pos1[i - 1])
        return -1 if ans == inf else ans

    # 计算字符串 p 的 pi 数组
    def calc_pi(self, p: str) -> List[int]:
        pi = [0] * len(p)
        cnt = 0
        for i in range(1, len(p)):
            v = p[i]
            while cnt > 0 and p[cnt] != v:
                cnt = pi[cnt - 1]
            if p[cnt] == v:
                cnt += 1
            pi[i] = cnt
        return pi

    # 在文本串 s 中查找模式串 p，返回所有成功匹配的位置（p[0] 在 s 中的下标）
    def kmp_search(self, s: str, p: str) -> List[int]:
        if not p:
            # s 的所有位置都能匹配空串，包括 len(s)
            return list(range(len(s) + 1))

        pi = self.calc_pi(p)
        pos = []
        cnt = 0
        for i, v in enumerate(s):
            while cnt > 0 and p[cnt] != v:
                cnt = pi[cnt - 1]
            if p[cnt] == v:
                cnt += 1
            if cnt == len(p):
                pos.append(i - len(p) + 1)
                cnt = pi[cnt - 1]
        return pos

作者：灵茶山艾府
链接：https://leetcode.cn/problems/shortest-matching-substring/solutions/3076453/xian-xing-zuo-fa-kmpmei-ju-zhong-jian-sa-5qow/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。