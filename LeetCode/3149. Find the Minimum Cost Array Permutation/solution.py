class Solution:
    def findPermutation(self, a: List[int]) -> List[int]:
        n = len(a)
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(s: int, j: int) -> int:
            if s == (1 << n) - 1:
                # 所有位置都填完了，最后一个位置是下标 j
                return abs(j - a[0])
            res = inf
            # 枚举当前位置填下标 k
            for k in range(1, n):
                if s >> k & 1 == 0:  # k 之前没填过
                    res = min(res, dfs(s | 1 << k, k) + abs(j - a[k]))
            return res

        ans = []
        # 原理见上面贴的题解链接
        def make_ans(s: int, j: int) -> None:
            ans.append(j)
            if s == (1 << n) - 1:
                return
            final_res = dfs(s, j)
            for k in range(1, n):
                if s >> k & 1 == 0 and dfs(s | 1 << k, k) + abs(j - a[k]) == final_res:
                    make_ans(s | 1 << k, k)
                    break
        make_ans(1, 0)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-the-minimum-cost-array-permutation/solutions/2775272/zhuang-ya-dpcong-ji-yi-hua-sou-suo-dao-d-s9t5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        perm = [-1]*n  
        ans = [inf]
        candidates = [[]]
        visited = [0]*n 
        def dfs(i,cur):
            # print(i,cur,perm,visited)
            if i == n:
                cur += abs(perm[n-1]-nums[perm[0]])
                if cur < ans[0]:
                    ans[0] = cur
                    candidates[0] = perm[:]
                return

            for a in range(n):
                if visited[a] == 1: continue
                visited[a] = 1
                perm[i] = a  
                if i > 0:
                    cur += abs(perm[i-1]-nums[perm[i]])
                if cur < ans[0]:
                    dfs(i+1,cur)
                if i > 0:
                    cur -= abs(perm[i-1]-nums[perm[i]])
                perm[i] = -1
                visited[a] = 0 
            return

        dfs(0,0)
        # print(ans,perm)
        return candidates[0]
