# class Solution:
#     def beautifulSubstrings(self, s: str, k: int) -> int:
#         n = len(s)
#         arr = []
#         for ch in s:
#             if ch in "aeiou":
#                 arr.append(1)
#             else:
#                 arr.append(0)
#         ans = 0
#         for i in range(n):
#             cnt = 0
#             for j in range(i,n):
#                 cnt += arr[j]
#                 if 2*cnt == (j-i+1) and (cnt*cnt)%k == 0:
#                     ans += 1 
#         return ans 

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        k = self.sqrt(k * 4)
        cnt = Counter([(k - 1, 0)])  # k-1 和 -1 同余
        ans = pre_sum = 0
        for i, v in enumerate(s):
            pre_sum += 1 if v in "aeiou" else -1
            p = (i % k, pre_sum)
            ans += cnt[p]
            cnt[p] += 1
        return ans

    def sqrt(self, n: int) -> int:
        res = 1
        i = 2
        while i * i <= n:
            i2 = i * i
            while n % i2 == 0:
                res *= i
                n //= i2
            if n % i == 0:
                res *= i
                n //= i
            i += 1
        if n > 1:
            res *= n
        return res


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/circle/discuss/ip8jWQ/view/hLnPbj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。