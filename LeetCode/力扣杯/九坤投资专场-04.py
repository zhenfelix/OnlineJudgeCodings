# from functools import lru_cache
# class Solution:
#     def chipGame(self, nums: List[int], kind: int) -> float:
#         n = len(nums)
#         nums.sort(reverse=True)
#         target = tuple(nums)

#         res = 0
#         dp = {tuple(): 1}
#         tot = sum(nums)
#         for _ in range(tot):
#             ndp = Counter()
#             for cur, prob in dp.items():
#                 tmp = list(cur)
#                 fail = 0
#                 j = -1
#                 for i, val in enumerate(tmp):
#                     if i+1 < len(tmp) and tmp[i] == tmp[i+1]:
#                         continue
#                     if tmp[j+1] == target[j+1]:
#                         fail += i-j
#                     j = i
#                 if len(tmp) == n:
#                     fail += kind-n
#                 # print(cur,prob,fail,kind/(kind-fail))
#                 res += prob*kind/(kind-fail)
#                 j = -1
#                 for i, val in enumerate(tmp):
#                     if i+1 < len(tmp) and tmp[i] == tmp[i+1]:
#                         continue
#                     if tmp[j+1] < target[j+1]:
#                         tmp[j+1] += 1
#                         ndp[tuple(tmp)] += prob*(i-j)/(kind-fail)
#                         tmp[j+1] -= 1
#                     j = i
#                 if len(tmp) < n:
#                     tmp.append(1)
#                     ndp[tuple(tmp)] += prob*(kind-len(tmp)+1)/(kind-fail)
#             dp = ndp


#         return res


# from functools import lru_cache
# class Solution:
#     def chipGame(self, nums: List[int], kind: int) -> float:
#         nums.sort(reverse=True)
#         while len(nums) < kind:
#             nums.append(0)
#         target = tuple(nums)

#         start = tuple([0]*kind)
#         res = 0
#         dp = {start: 1}
#         tot = sum(nums)
#         for _ in range(tot):
#             ndp = Counter()
#             for cur, prob in dp.items():
#                 tmp = list(cur)
#                 fail = 0
#                 j = -1
#                 for i in range(kind):
#                     if i+1 < kind and tmp[i] == tmp[i+1]:
#                         continue
#                     if tmp[j+1] == target[j+1]:
#                         fail += i-j
#                     j = i
#                 # print(cur,prob,fail,kind/(kind-fail))
#                 res += prob*kind/(kind-fail)
#                 j = -1
#                 for i in range(kind):
#                     if i+1 < kind and tmp[i] == tmp[i+1]:
#                         continue
#                     if tmp[j+1] < target[j+1]:
#                         tmp[j+1] += 1
#                         ndp[tuple(tmp)] += prob*(i-j)/(kind-fail)
#                         tmp[j+1] -= 1
#                     j = i
#                 # for nxt, val in success.items():
#                 #     ndp[nxt] += prob*val/(kind-fail)
#             dp = ndp


#         return res

# https://leetcode.cn/circle/article/l8SRYI/
bottom up + pruning + no sort

class Solution:
    def chipGame(self, nums: List[int], kind: int) -> float:
        nums.sort(reverse=True)
        while len(nums) < kind:
            nums.append(0)
        target = tuple(nums)

        start = tuple([0]*kind)
        res = 0
        dp = {start: 1}
        tot = sum(nums)
        for _ in range(tot):
            ndp = Counter()
            for cur, prob in dp.items():
                tmp = list(cur)
                fail = 0
                success = Counter()
                j = -1
                for i in range(kind):
                    if i+1 < kind and tmp[i] == tmp[i+1]:
                        continue
                    if tmp[j+1] == target[j+1]:
                        fail += i-j
                    else:
                        tmp[j+1] += 1
                        success[tuple(tmp)] += i-j
                        tmp[j+1] -= 1
                    j = i
                # print(cur,prob,fail,kind/(kind-fail))
                res += prob*kind/(kind-fail)
                for nxt, val in success.items():
                    ndp[nxt] += prob*val/(kind-fail)
            dp = ndp


        return res







# https://leetcode.cn/contest/ubiquant2022/ranking/

from functools import lru_cache
class Solution:
    def chipGame(self, nums: List[int], kind: int) -> float:
        nums.sort(reverse=True)
        while len(nums) < kind:
            nums.append(0)
        nums = tuple(nums)

        @lru_cache(None)
        def dfs(s):
            if s == nums:
                return 0
            state = list(s)
            E = 0
            vain = 0
            for i in range(len(state)):
                new_state = copy.copy(state)
                new_state[i] += 1
                new_state.sort(reverse=True)
                new_state = tuple(new_state)
                if not all(new_state[j] <= nums[j] for j in range(kind)):
                    vain += 1 / kind
                    continue
                E += (dfs(new_state) + 1) / kind
            return (vain + E) / (1 - vain)

        return dfs(tuple([0] * kind))


# 作者：长夜
# 链接：https://leetcode.cn/circle/article/l8SRYI/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
