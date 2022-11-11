class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0
        n = len(costs)
        q = []
        if candidates*2 >= n:
            for i, c in enumerate(costs):
                heapq.heappush(q,(c,i))
            for _ in range(k):
                c, i = heapq.heappop(q)
                ans += c  
        else:
            for i in range(candidates):
                heapq.heappush(q,(costs[i],i,0))
                heapq.heappush(q,(costs[n-i-1],n-i-1,1))
            left, right = candidates-1, n-candidates
            for _ in range(k):
                c, i, flag = heappop(q)
                ans += c 
                if left+1 < right:
                    if flag == 0:
                        left += 1
                        heapq.heappush(q,(costs[left],left,0))
                    else:
                        right -= 1
                        heapq.heappush(q,(costs[right],right,1))
        return ans 



class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans, n = 0, len(costs)
        if candidates * 2 < n:
            pre = costs[:candidates]
            heapify(pre)
            suf = costs[-candidates:]
            heapify(suf)
            i, j = candidates, n - 1 - candidates
            while k and i <= j:
                if pre[0] <= suf[0]:
                    ans += heapreplace(pre, costs[i])
                    i += 1
                else:
                    ans += heapreplace(suf, costs[j])
                    j -= 1
                k -= 1
            costs = pre + suf
        costs.sort()
        return ans + sum(costs[:k])  # 也可以用快速选择算法求前 k 小


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/HhkSf4/view/pK06Qb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。