class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        tot = sum(nums)
        n = len(nums)
        mp = {0: 0}
        s = 0
        for i in range(n)[::-1]:
            s += nums[i]
            mp[s] = n-i
        s = 0
        ans = inf 
        pre = {0: 0}
        for i in range(n+1):
            if i > 0:
                s += nums[i-1]
            if target >= s:
                r = (target-s)%tot
                if r in mp:
                    ans = min(ans,i+mp[r]+(target-s)//tot*n)
            if s-target in pre:
                ans = min(ans,i-pre[s-target])
            pre[s] = i  
        return ans if ans < inf else -1



class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)
        ans = inf
        left = s = 0
        for right in range(n * 2):
            s += nums[right % n]
            while s > target % total:
                s -= nums[left % n]
                left += 1
            if s == target % total:
                ans = min(ans, right - left + 1)
        return ans + target // total * n if ans < inf else -1


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/9idUqp/view/QFZ1w1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。