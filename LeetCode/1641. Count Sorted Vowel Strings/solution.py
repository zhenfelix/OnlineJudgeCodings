# class Solution:
#     def countVowelStrings(self, n: int) -> int:
#         dp = [1]*5
#         for _ in range(1,n):
#             for i in range(5)[::-1]:
#                 dp[i] += sum(dp[:i])
#         return sum(dp)

class Solution:
    # def countVowelStrings(self, n: int) -> int:
    #     dp = [1]*5
    #     for _ in range(n):
    #         for i in range(1,5):
    #             dp[i] += dp[i-1]
    #     return dp[-1]
    
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        for i in range(n):
            dp = accumulate(dp)
        return list(dp)[-1]


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n + 4, 4)


# 作者：zerotrac2
# 链接：https://leetcode-cn.com/problems/count-sorted-vowel-strings/solution/tong-ji-zi-dian-xu-yuan-yin-zi-fu-chuan-de-shu-mu-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。