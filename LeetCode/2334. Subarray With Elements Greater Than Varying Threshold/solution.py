class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        nums.append(0)
        st = [-1]
        for i in range(n+1):
            while st and nums[st[-1]] > nums[i]:
                cur = st.pop()
                sz = i-st[-1]-1
                # print(cur,sz,nums[cur])
                if nums[cur] > threshold/sz:
                    return sz 
            st.append(i)
        return -1




class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        fa = list(range(n + 1))
        sz = [1] * (n + 1)
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        for num, i in sorted(zip(nums, range(n)), reverse=True):
            j = find(i + 1)
            fa[i] = j  # 合并 i 和 i+1
            sz[j] += sz[i]
            if num > threshold // (sz[j] - 1):
                return sz[j] - 1
        return -1


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/subarray-with-elements-greater-than-varying-threshold/solution/by-endlesscheng-j6pp/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。