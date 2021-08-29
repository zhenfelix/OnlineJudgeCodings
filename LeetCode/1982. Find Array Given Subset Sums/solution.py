class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        bias = -min(sums)
        sums = [x+bias for x in sums]
        arr = [0]
        res = []
        cc = Counter(sums)
        cc[0] -= 1
        for x in sorted(sums):
            if cc[x] > 0:
                res.append(x)
                n = len(arr)
                for i in range(n):
                    y = arr[i]
                    cc[x+y] -= 1
                    arr.append(x+y)
        if bias == 0:
            return res 
        n = len(res)
        for state in range(1<<n):
            if sum(res[i] for i in range(n) if (state>>i)&1) == bias:
                return [-res[i] if (state>>i)&1 else res[i] for i in range(n)]
        return []


# TLE
# class Solution:
#     def recoverArray(self, n: int, sums: List[int]) -> List[int]:
#         res = []

#         def check(x, arr, cc):
#             flag = True
#             for y in arr:
#                 cc[y+x] -= 1
#                 if cc[y+x] < 0:
#                     flag = False
#             for y in arr:
#                 cc[y+x] += 1
#             return flag 


#         def dfs(idx, path, arr, cc):
#             # print(idx,path,arr,cc)
#             if idx == n:
#                 # print(path)
#                 res.append(path[:])
#                 return True
#             for x in sums:
#                 if cc[x] <= 0:
#                     continue
#                 if check(x, arr, cc):
#                     path.append(x)
#                     sz = len(arr)
#                     for i in range(sz):
#                         cc[arr[i]+x] -= 1
#                         arr.append(arr[i]+x)
#                     if dfs(idx+1, path, arr, cc):
#                         return True
#                     for i in range(sz):
#                         arr.pop()
#                         cc[arr[i]+x] += 1
#                     path.pop()
#             return False

#         dfs(0,[],[0],Counter(sums))
#         return res[-1]

