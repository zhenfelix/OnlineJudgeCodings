class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        ans = []
        for a in nums:
            if a:
                ans.append(a)
        m = len(ans)
        for i in range(n-m):
            ans.append(0)
        return ans 

class Solution:
    def applyOperations(self, a: List[int]) -> List[int]:
        j, n = 0, len(a)
        for i in range(n - 1):
            if a[i]:
                if a[i] == a[i + 1]:
                    a[i] *= 2
                    a[i + 1] = 0
                a[j] = a[i]  # 非零数字排在前面
                j += 1
        if a[-1]:
            a[j] = a[-1]
            j += 1
        for i in range(j, n):
            a[i] = 0
        return a


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/HhkSf4/view/pK06Qb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。