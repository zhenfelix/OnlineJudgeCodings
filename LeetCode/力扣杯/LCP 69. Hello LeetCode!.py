# https://leetcode.cn/u/freetime430/
class Solution:
    def Leetcode(self, words: List[str]) -> int:
        target = "".join(sorted(list("helloleetcode")))
        self.vis = {}
        self.words = words
        self.words.append("")
        return self.dfs(words[0], 0, target)

    def dfs(self, word, idx, target):
        if not target:
            return 0
        if idx == len(self.words)-1:
            return -1
        key = (word, idx, target)
        if key not in self.vis:
            self.vis[key] = self.dfs(self.words[idx+1], idx+1, target)
            for i in range(len(word)):
                j = target.find(word[i])
                if j != -1:
                    res = self.dfs(word[:i] + word[i+1:], idx, target[:j]+target[j+1:])
                    if res != -1:
                        if self.vis[key] == -1 or self.vis[key] > res + i * (len(word)-i-1):
                            self.vis[key] = res + i * (len(word)-i-1)
        return self.vis[key]



class Solution:
    def Leetcode(self, words: List[str]) -> int:
        cost = [Counter() for _ in range(8)]
        for sz in range(8):
            cost[sz][0] = 0 
            for s in range(1,1<<(sz+1)):
                cost[sz][s] = float('inf')
                tot, cnt = 0, 0
                for i in range(sz+1):
                    if (s>>i)&1:
                        tot += 1
                for i in range(sz+1):
                    if (s>>i)&1:
                        r, l = i-cnt, sz+1-i-(tot-cnt)
                        cost[sz][s] = min(cost[sz][s], cost[sz][s-(1<<i)]+l*r)
                        cnt += 1
        # print(cost[7][130])
        target = "helloleetcode"
        target = sorted(list(target))
        t = len(target)
        n = len(words)
        states = defaultdict(list)
        for i in range(n):
            m = len(words[i])            
            for cur in range(1<<m):
                cc = Counter(target)
                flag = True
                for j in range(m):
                    if (cur>>j)&1:
                        if cc[words[i][j]] == 0:
                            flag = False
                            break
                        cc[words[i][j]] -= 1
                if flag:
                    states[i].append(cur)
            
        # print(states)


        @lru_cache(None)
        def dfs(i, s):
            if i == n:
                return 0 if s == 0 else float('inf')
            # tmp = defaultdict(list)
            # for j in range(t):
            #     if (s>>j)&1:
            #         tmp[target[j]].append(j)

            m = len(words[i])
            res = float('inf')
            for cur in states[i]:
            # for cur in range(1<<m):
                ws = []
                for j in range(m):
                    if (cur>>j)&1:
                        ws.append(words[i][j])
                ws.sort()
                flag = True
                k = 0
                nxt = s
                for ch in ws:
                    while k < t and (target[k] != ch or ((nxt>>k)&1) != 1):
                        k += 1
                    if k >= t:
                        flag = False
                        break
                    nxt -= (1<<k)
                if flag:
                # if flag and cost[m-1][cur] < res:
                    res = min(res, dfs(i+1, nxt)+cost[m-1][cur])
            return res
        ans = dfs(0,(1<<t)-1)
        return ans if ans < float('inf') else -1