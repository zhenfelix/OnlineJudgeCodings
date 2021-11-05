class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        arr = []
        for i, x in enumerate(nums):
            if x == 1:
                arr.append(i)
        n = len(arr)
        presums = [0]
        for i in arr:
            presums.append(presums[-1]+i)
        cnt_left = k//2
        cnt_right = k-cnt_left
        res = float('inf')
        for j in range(k-1,n):
            p = j-k
            i = p+cnt_left
            res = min(res, presums[j+1]+presums[p+1]-2*presums[i+1]-arr[i+1]*(k%2)-(1+cnt_left)*cnt_left//2-(cnt_right-1)*cnt_right//2)
        return res



class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        n = len(nums)
        g, total, count = list(), [0], -1
        
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
                g.append(i - count)
                total.append(total[-1] + g[-1])
        
        m, ans = len(g), float("inf")
        
        for i in range(m - k + 1):
            mid = (i + i + k - 1) // 2
            q = g[mid]
            ans = min(ans, (2 * (mid - i) - k + 1) * q + (total[i + k] - total[mid + 1]) - (total[mid] - total[i]))
        
        return ans



# 作者：zerotrac2
# 链接：https://leetcode-cn.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/solution/de-dao-lian-xu-k-ge-1-de-zui-shao-xiang-lpa9i/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。        


# class Solution:
#     def minMoves(self, nums: List[int], k: int) -> int:
#         q = deque()
#         res = float('inf')
#         n = len(nums)
#         presum = [0]*n
#         total = 0
#         for i, cur in enumerate(nums):
#             if cur == 1:
#                 q.append(i)
#                 total += i 
#             presum[i] = total
#             if len(q) > k:
#                 q.popleft()
#             if cur == 1 and len(q) == k:
#                 mid = q[k//2]
#                 left, right = q[0], q[-1]
#                 cnt_left, cnt_right = k//2, k-1-k//2
#                 tmp = 0
#                 tmp += presum[right]-presum[mid]-cnt_right*mid-(cnt_right+1)*cnt_right//2
#                 # print(tmp)
#                 tmp += (mid-left)*(cnt_left+1)-(-presum[left]+presum[mid]-cnt_left*left)-(cnt_left+1)*cnt_left//2
#                 # print(tmp)
#                 res = min(res, tmp)
#         #         print(q,mid, cnt_left, cnt_right,tmp)
#         # print(presum,res)
#         return res 

