class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        groups = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            groups[a].append(b)

        ans = 0
        extra = [0] * (n + 2)
        b = [n + 1, n + 1]  # 维护最小 b 和次小 b
        for a in range(n, 0, -1):
            b = sorted(b + groups[a])[:2]
            ans += b[0] - a
            extra[b[0]] += b[1] - b[0]

        return ans + max(extra)

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximize-subarrays-after-removing-one-conflicting-pair/solutions/3603047/mei-ju-zuo-duan-dian-wei-hu-zui-xiao-ci-4nvu6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        arr = [[] for _ in range(n)]
        for i, (a,b) in enumerate(conflictingPairs):
            a -= 1
            b -= 1
            arr[a].append(i)
            arr[b].append(i)
        cc1 = Counter()
        cc2 = Counter()
        j1 = j2 = s = 0
        delta = defaultdict(int)
        ch1 = set()
        ch2 = set()
        for i in range(n):
            for ch in arr[i]:
                cc1[ch] += 1
                if cc1[ch] == 2:
                    ch1.add(ch)
                cc2[ch] += 1
                if cc2[ch] == 2:
                    ch2.add(ch)
            while len(ch1) > 0:
                for ch in arr[j1]:
                    cc1[ch] -= 1
                    if cc1[ch] == 1:
                        ch1.remove(ch)
                j1 += 1
            s += i-j1+1
            while len(ch2) > 1:
                for ch in arr[j2]:
                    cc2[ch] -= 1
                    if cc2[ch] == 1:
                        ch2.remove(ch)
                j2 += 1
            if len(ch2) == 1:
                ch = ch2.pop()
                delta[ch] += i-j2-(i-j1)
                ch2.add(ch)
        ans = 0
        for i, _ in enumerate(conflictingPairs):
            ans = max(ans,s+delta[i])
        return ans 

