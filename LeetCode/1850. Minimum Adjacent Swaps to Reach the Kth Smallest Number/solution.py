# class Solution:
#     def getMinSwaps(self, num: str, k: int) -> int:
#         origin = list(num)
#         num = list(num)
#         n = len(num)
#         while k:
#             i = n-1
#             while i and num[i-1] >= num[i]:
#                 i -= 1
#             if i == 0:
#                 return -1
#             j = i-1
#             i = n-1
#             while num[i] <= num[j]:
#                 i -= 1
#             num[j], num[i] = num[i], num[j]
#             left, right = j+1, n-1
#             while left < right:
#                 num[left], num[right] = num[right], num[left]
#                 left += 1
#                 right -= 1
#             k -= 1
#         res = 0
#         mp = defaultdict(list)
#         for i in range(n):
#             j = i 
#             while num[i] != origin[j]:
#                 j += 1
#                 res += 1
#             while j > i:
#                 origin[j-1], origin[j] = origin[j], origin[j-1]
#                 j -= 1
#         # print("".join(num))
#         return res


class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def nxt_perm(num: list) -> list:
            i = n - 1
            while i > 0 and num[i-1] >= num[i]:
                i -= 1
            j = i
            while j < n and num[i-1] < num[j]:
                j += 1
            num[i-1], num[j-1] = num[j-1], num[i-1]
            num[i:] = num[i:][::-1]
            return num

        n = len(num)
        nxt_k_num = list(num)
        for _ in range(k):
            nxt_k_num = nxt_perm(nxt_k_num)

        ans = 0
        num = list(num)
        for i in range(n):
            j = i
            while j < n and nxt_k_num[i] != num[j]:
                j += 1
            ans += j - i
            num[i:j+1] = [num[j]] + num[i:j]
        return ans