class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [x&1 for x in nums]
        cc = Counter(nums)
        if abs(cc[0]-cc[1]) > 1: return -1
        def check(pre):
            tmp = nums[:]
            ans = 0
            j = 0
            for i in range(n):
                j = max(j,i)
                if tmp[i] == 0:
                    pre += 1
                else:
                    if pre > 0:
                        ans += pre-1
                        pre -= 1
                    else:
                        while j < n and tmp[j] == 1:
                            j += 1
                        tmp[i], tmp[j] = tmp[j], tmp[i]
                        pre += 1
                        ans += j-i
            return ans 
        if cc[1] > cc[0]:
            return check(1)
        elif cc[1] < cc[0]:
            return check(0)
        return min(check(0),check(1))


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        pos1 = [i for i, x in enumerate(nums) if x % 2]  # 车（奇数）的下标

        n = len(nums)
        m = len(pos1)

        # start=0 表示车要去偶数下标，start=1 表示车要去奇数下标
        def calc(start: int) -> int:
            # (n-start+1)//2 表示偶数（奇数）下标的个数
            if (n - start + 1) // 2 != m:
                return inf
            return sum(abs(i - j) for i, j in zip(range(start, n, 2), pos1))

        ans = min(calc(0), calc(1))
        return -1 if ans == inf else ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/minimum-adjacent-swaps-to-alternate-parity/solutions/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。