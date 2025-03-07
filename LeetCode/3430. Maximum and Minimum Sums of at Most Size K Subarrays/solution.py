class Solution:
    # 计算最小值的贡献
    def sumSubarrayMins(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 左边界 left[i] 为左侧严格小于 nums[i] 的最近元素位置（不存在时为 -1）
        left = [-1] * n
        # 右边界 right[i] 为右侧小于等于 nums[i] 的最近元素位置（不存在时为 n）
        right = [n] * n
        st = []
        for i, x in enumerate(nums):
            while st and x <= nums[st[-1]]:
                right[st.pop()] = i  # i 是栈顶的右边界
            if st:
                left[i] = st[-1]
            st.append(i)

        ans = 0
        for i, (x, l, r) in enumerate(zip(nums, left, right)):
            if r - l - 1 <= k:
                cnt = (i - l) * (r - i)
                ans += x * cnt  # 累加贡献
            else:
                l = max(l, i - k)
                r = min(r, i + k)
                # 左端点 > r-k 的子数组个数
                cnt = (r - i) * (i - (r - k))
                # 左端点 <= r-k 的子数组个数
                cnt2 = (l + r + k - i * 2 + 1) * (r - l - k) // 2
                ans += x * (cnt + cnt2)  # 累加贡献
        return ans

    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        ans = self.sumSubarrayMins(nums, k)
        # 所有元素取反，就可以复用同一份代码求最大值的贡献了
        ans -= self.sumSubarrayMins([-x for x in nums], k)
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/solutions/3051552/gong-xian-fa-dan-diao-zhan-pythonjavacgo-9gz3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



def doit1(l,r,k):
    ans = 0
    for p in range(l):
        ans += min(r,max(0,k-p))
    return ans 

def doit2(l,r,k):

    ans = 0
    p1 = k-r
    if p1 > 0:
        if p1 > l-1:
            return l*r 
        ans += p1*r
    p1 = max(0,p1)
    p2 = min(k,l-1)
    q1 = k-p1
    q2 = k-p2  
    if p2 >= p1:
        ans += (q1+q2)*(p2-p1+1)//2
    return ans 

# def doit2(l, r, k):
#     ans = 0
    
#     # 第一部分：处理 p <= k - r 的情况，贡献 r
#     if k >= r:
#         part1_count = min(k - r + 1, l)
#         part1_count = max(part1_count, 0)  # 确保非负
#         ans += part1_count * r
    
#     # 第二部分：处理 k - r + 1 <= p <= min(k-1, l-1) 的情况，贡献 (k - p)
#     a = max(k - r + 1, 0)
#     b = min(k - 1, l - 1)
#     if a <= b:
#         sum_part2 = ( (k - a) + (k - b) ) * (b - a + 1) // 2
#         ans += sum_part2
    
#     return ans

# for l in range(1,10):
#     for r in range(1,10):
#         for k in range(1,10):
#             a1 = doit1(l,r,k)
#             a2 = doit2(l,r,k)
#             if a1 != a2:
#                 print(l,r,k,a1,a2)



class Solution:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        nums.append(0)
        n = len(nums)
        def great(x,y):
            return x>y  
        def less(x,y):
            return x<y  
        def calc(op):
            st = [-1]
            ans = 0
            L = list(range(n))
            for i in range(n):
                while st and op(nums[i],nums[st[-1]]):
                    j = st.pop()
                    l = j-L[j]
                    r = i-j
                    # print(l,r,k)
                    # print(doit1(l,r,k))
                    ans += doit2(l,r,k)*nums[j]
                    # print(doit2(l,r,k))
                    
                L[i] = st[-1]
                st.append(i)
            return ans 
        res = 0
        nums[-1] = inf 
        res += calc(great)
        nums[-1] = -inf
        res += calc(less)
        return res

