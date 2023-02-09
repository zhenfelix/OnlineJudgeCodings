# LC2447 2447. Number of Subarrays With GCD Equal to K


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            g = k
            for j in range(i,n):
                v = nums[j]
                if k%v:
                    break
                g = gcd(g,k//v)
                if g == 1:
                    ans += 1 
        return ans 



class Solution:

    def subarrayLCM(self, nums: List[int], k: int) -> int:

        ans, n = 0, len(nums)

        for i in range(n):

            res = 1

            for j in range(i, n):

                res = lcm(res, nums[j])

                if k % res: break  # 剪枝：LCM 必须是 k 的因子

                if res == k: ans += 1

        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/number-of-subarrays-with-lcm-equal-to-k/solutions/1965427/by-endlesscheng-3qnt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。