# class Solution:
#     def findEvenNumbers(self, digits: List[int]) -> List[int]:
#         ans = set()
#         for x, y, z in permutations(digits, 3): 
#             if x != 0 and z & 1 == 0: 
#                 ans.add(100*x + 10*y + z) 
#         return sorted(ans)


# class Solution:
#     def findEvenNumbers(self, digits: List[int]) -> List[int]:
#         cc = Counter(digits)
#         digits = []
#         for k, v in cc.items():
#             v = min(v,3)
#             digits += [k]*v
#         res = set()
#         def dfs(i,path):
#             nonlocal res
#             if i == 3:
#                 val = int(''.join(str(digits[x]) for x in path))
#                 if val >= 100 and val%2 == 0:
#                     res.add(val)
#                 return
#             for j in range(len(digits)):
#                 if j not in path:
#                     dfs(i+1, path+[j])
#             return
#         dfs(0,[])
#         return sorted(list(res))


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cc = Counter(digits)
        res = []
        def dfs(i,val):
            nonlocal res
            if i == 3:
                if val >= 100 and val%2 == 0:
                    res.append(val)
                return
            for j in range(10):
                if cc[j]:
                    cc[j] -= 1
                    dfs(i+1, val*10+j)
                    cc[j] += 1
            return
        dfs(0,0)
        return res


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = collections.Counter(digits)
        return [num for num in range(100, 1000, 2) if all(str(num).count(ch) <= cnt[int(ch)] for ch in set(str(num)))]


# 作者：吴自华
# 链接：https://leetcode-cn.com/circle/discuss/PrR8pS/view/5iH0hw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。