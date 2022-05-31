class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        res = 0
        nums.append(0)
        nums.append(float('inf'))
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        # print(nums)
        for i in range(1,n):
            delta = nums[i]-nums[i-1]-1
            cnt = min(delta,k)
            res += (nums[i-1]+1+nums[i-1]+cnt)*cnt//2
            k -= cnt
            if k == 0:
                break
            # print(res,k,delta,cnt)
        return res


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums)) + [int(2e9)]
        s = 0
        for i, num in enumerate(nums):
            if num - 1 - i >= k:
                return (k + i) * (k + i + 1) // 2 - s
            s += num
        
        return -1


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/c8HUDh/view/eCf0rc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。