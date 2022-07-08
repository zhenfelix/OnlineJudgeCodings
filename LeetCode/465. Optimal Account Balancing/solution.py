# from collections import Counter, defaultdict

# class Solution:
#     def minTransfers(self, transactions: List[List[int]]) -> int:
#         persons = set()
#         debt = Counter()
#         for e in transactions:
#             debt[e[0]] += e[2]
#             debt[e[1]] -= e[2]
#             persons.add(e[0])
#             persons.add(e[1])

#         def dfs(cur,cnts):
#             if cnts >= ans[0]:
#                 return
#             if debt[cur] == 0:
#                 for person in persons:
#                     if debt[person] != 0:
#                         cur = person
#                         break
            
#             if debt[cur] == 0:
#                 ans[0] = min(ans[0],cnts)
#                 return
            
#             tmp = debt[cur]
#             for nxt in persons:
#                 if debt[nxt]*debt[cur] < 0:
#                     debt[cur] -= tmp
#                     debt[nxt] += tmp
#                     dfs(nxt,cnts+1)
#                     debt[nxt] -= tmp
#                     debt[cur] += tmp
#             return

#         ans = [float('inf')]
#         cc = 0
#         mp = defaultdict(list)
#         for k, v in debt.items():
#             if v != 0 and len(mp[-v]) > 0:
#                 cc += 1
#                 idx = mp[-v].pop()
#                 debt[idx] = 0
#                 debt[k] = 0
#                 # del debt[k]
#                 # del debt[idx]
#             elif v != 0:
#                 mp[v] += [k]

#         # print(debt)
#         dfs(transactions[0][0],cc)
#         return ans[0]


from collections import Counter, defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        persons = set()
        debt = Counter()
        for e in transactions:
            debt[e[0]] += e[2]
            debt[e[1]] -= e[2]
            persons.add(e[0])
            persons.add(e[1])

        ans = [float('inf')]
        cc = 0
        # mp = defaultdict(list)
        # for k, v in debt.items():
        #     if v != 0 and len(mp[-v]) > 0:
        #         cc += 1
        #         idx = mp[-v].pop()
        #         debt[idx] = 0
        #         debt[k] = 0
        #         # del debt[k]
        #         # del debt[idx]
        #     elif v != 0:
        #         mp[v] += [k]
        debt = list(debt.values())
        debt = [a for a in debt if a != 0]
        n = len(debt)

        def dfs(cur,cnts):
            if cnts >= ans[0]:
                return
            while cur < n and debt[cur] == 0:
                cur += 1
            
            if cur == n:
                ans[0] = min(ans[0],cnts)
                return
            
            for nxt in range(cur+1,n):
                if debt[nxt]*debt[cur] < 0:
                    debt[nxt] += debt[cur]
                    dfs(cur+1,cnts+1)
                    debt[nxt] -= debt[cur]
            return

        # print(debt)
        # print(cc)
        dfs(0,cc)
        return ans[0]





解题思路

首先我们可以统计每个人的总金额。如果一个人的总金额为000，显然这个人将不需要参与交易。

剩下来的人总金额要么为正，要么为负。我们可以注意到，对于一组kkk个人，如果他们的合计总金额为000，那么我们至多可以通过k−1k-1k−1次交易来平账：我们可以先把所有的欠款统一还给一个人，再由他分配给其他需要收款的人。

因此，我们应该将这些人分成尽可能多的合计总金额为000的组。我们可以使用状态压缩动态规划，通过枚举子集的方式来进行求解。

令dp[state]dp[state]dp[state]表示statestatestate所对应的这组人所能够分成的最多的组数。注意我们只有在sum[state]=0sum[state]=0sum[state]=0的情况下才去枚举statestatestate的子集。转移方程为dp[state]=max⁡sub⫋state(dp[sub])+1dp[state]=\max_{sub\subsetneqq state}(dp[sub])+1dp[state]=maxsub⫋state​(dp[sub])+1。

最后的答案就是n−dp[2n−1]n-dp[2^n-1]n−dp[2n−1]，其中nnn是总金额不为000的人数。

作者：lucifer1004
链接：https://leetcode.cn/problems/optimal-account-balancing/solution/zhuang-tai-ya-suo-dong-tai-gui-hua-by-lu-2qrt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debt = Counter()
        for e in transactions:
            debt[e[0]] += e[2]
            debt[e[1]] -= e[2]

        debt = list(debt.values())
        debt = [a for a in debt if a != 0]
        n = len(debt)
        # print(debt)

        tot = 1<<n 
        score = [0]*tot
        dp = [-float('inf')]*tot
        dp[0] = 0 
        val = defaultdict(int)
        for i in range(n):
            val[1<<i] = debt[i]
        for s in range(1,tot):
            score[s] = score[s-(s&-s)] + val[s&-s]
        
        for s in range(1,tot):
            if score[s] != 0:
                collections
            cur = mask = s 
            while cur:
                if score[cur] == 0:
                    dp[s] = max(dp[s], 1+dp[s^cur])
                cur = (cur-1)&mask
        # print(dp)
        return n-dp[tot-1]


        
class Solution:
        def minTransfers(self, transactions: List[List[int]]) -> int:
            debt = Counter()
            for e in transactions:
                debt[e[0]] += e[2]
                debt[e[1]] -= e[2]

            debt = list(debt.values())
            debt = [a for a in debt if a != 0]
            n = len(debt)
            # print(debt)

            @cache
            def dfs(state, cur):
                if state == (1<<n)-1:
                    return 0
                res = float('inf')
                for i in range(n):
                    if (state>>i)&1 == 0:
                        res = min(res, (cur != 0) + dfs(state|(1<<i), cur+debt[i]))
                return res 
            return dfs(0,0)