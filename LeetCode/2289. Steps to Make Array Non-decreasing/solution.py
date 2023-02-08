class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        mx = ans = 0
        n = len(nums)
        mx = nums[0]
        st = []
        dp = [0]*n 
        for i in range(1,n):
            if nums[i] < mx:
                cur = 0
                while st and nums[st[-1]] <= nums[i]:
                    cur = max(cur, dp[st.pop()])
                dp[i] = cur + 1
                st.append(i)
            else:
                st = []
                mx = nums[i]
            ans = max(ans, dp[i])
        return ans


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [i-1 for i in range(n)]
        nxt = [i+1 for i in range(n)]
        to_del = [i for i in range(1,n) if nums[i] < nums[i-1]]
        ans = 0

        def delete(node):
            pn, nn = pre[node], nxt[node]
            if pn >= 0:
                nxt[pn] = nn
            if nn < n:
                pre[nn] = pn

        while to_del:
            check = []
            for i in to_del:
                if not check or check[-1] != pre[i]:
                    check.append(pre[i])
                delete(i)
            to_del = []
            for p in check:
                nn = nxt[p]
                if nn < n and nums[p] > nums[nn]:
                    to_del.append(nn)
            ans += 1
        return ans



class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        ans, st = 0, []
        for num in nums:
            max_t = 0
            while st and st[-1][0] <= num:
                max_t = max(max_t, st.pop()[1])
            max_t = max_t + 1 if st else 0
            ans = max(ans, max_t)
            st.append((num, max_t))
        return ans


作者：endlesscheng
链接：https://leetcode.cn/problems/steps-to-make-array-non-decreasing/solution/by-endlesscheng-s2yc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。