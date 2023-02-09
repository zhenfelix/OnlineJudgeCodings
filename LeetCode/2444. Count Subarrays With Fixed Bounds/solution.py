class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        j, mi, mx = -1, -1, -1
        ans = 0
        for i in range(n):
            if nums[i] == minK:
                mi = i 
            if nums[i] == maxK:
                mx = i 
            if nums[i] < minK or nums[i] > maxK:
                mi = mx = j = i 
            ans += min(mi,mx)-j
        return ans


class Solution:
    def countSubarrays(self, nums: List[int], min_k: int, max_k: int) -> int:
        ans = 0
        min_i = max_i = i0 = -1
        for i, x in enumerate(nums):
            if x == min_k: min_i = i
            if x == max_k: max_i = i
            if not min_k <= x <= max_k: i0 = i  # 子数组不能包含 nums[i0]
            ans += max(min(min_i, max_i) - i0, 0)
            # 注：上面这行代码，改为手动算 min max 会更快
            # j = min_i if min_i < max_i else max_i
            # if j > i0: ans += j - i0
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/count-subarrays-with-fixed-bounds/solution/jian-ji-xie-fa-pythonjavacgo-by-endlessc-gag2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        left = cnt = mi = mx = res = 0
        pre = 0
        for right, v in enumerate(nums):
            if v == minK:
                mi += 1
            if v == maxK:
                mx += 1
            if v < minK or v > maxK:
                cnt += 1
                continue
            while (mi > 0 and mx > 0) or cnt > 0:
                w = nums[left]
                left += 1
                if cnt > 0:
                    pre = left
                if w < minK or w > maxK:
                    cnt -= 1
                if w == minK:
                    mi -= 1
                if w == maxK:
                    mx -= 1
            res += left-pre
        return res 

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        def check(inc = True):
            if inc:
                arr = nums+[-float('inf')]
            else:
                arr = nums+[float('inf')]
            st = [-1]
            left, right = list(range(n)), list(range(n))
            def cmp(op, a, b):
                if op:
                    return a > b
                else:
                    return a < b 
            for i, x in enumerate(arr):
                while st and cmp(inc, arr[st[-1]], x):
                    m = st.pop()
                    left[m] = st[-1]+1
                    right[m] = i-1
                        
                st.append(i)
            return left, right
        mileft, miright = check(True)
        mxleft, mxright = check(False)

        # print(mxleft, mxright)
        # print(mileft, miright)
        mx, mi = [], []
        res = 0
        for i in range(n)[::-1]:
            x = nums[i]
            if x == maxK:
                mx.append(i)
            if x == minK:
                mi.append(i)
            if i+1 < n and nums[i+1] == x:
                mileft[i+1] = mileft[i]
                mxleft[i+1] = mxleft[i]
            if x == maxK:
                mxlo, mxhi = mxleft[i], mxright[i]
                if mi:
                    j = mi[-1]
                    milo, mihi = mileft[j], miright[j]
                    if milo <= i and mxhi >= j:
                        lo = max(milo,mxlo)
                        hi = min(mihi, mxhi)
                        res += (i-lo+1)*(hi-j+1)
                
            elif x == minK:
                milo, mihi = mileft[i], miright[i]
                if mx:
                    j = mx[-1]
                    mxlo, mxhi = mxleft[j], mxright[j]
                    if mxlo <= i and mihi >= j:
                        lo = max(milo,mxlo)
                        hi = min(mihi,mxhi)
                        res += (i-lo+1)*(hi-j+1)
            
            
            
            
        return res 

