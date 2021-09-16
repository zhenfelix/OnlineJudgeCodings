from functools import lru_cache


def cut(start, end, x):
# 从start到end的路径将路口分成两个部分，判断x是在哪个部分
    if (start < end and start <= x <= end) or (start > end and not (end < x < start)):
        return -1
    return 1

def check(i, j, ii, jj):
# 判断i出发到j的路径和ii出发到jj的路径是否有效
    return i != j and ii != jj and i != ii and j != jj and cut(i,j,ii)*cut(i,j,jj) != -1


class Solution:
    def trafficCommand(self, directions: List[str]) -> int:
        mp = {'E': 0, 'S': 1, 'W': 2, 'N': 3}

        @lru_cache(None)
        def dfs(*states):
            if sum(states) == 0:
                return 0
            res = float('inf')

            def generate(i, path):
                if i == 4:
                    yield path
                    return
                yield from generate(i+1, path)
                if states[i] == 0:
                    return
                j = mp[directions[i][-states[i]]]
                cur = (i, j)
                for ii, jj in path:
                    if not check(i, j, ii, jj):
                        return
                yield from generate(i+1, path+[(i, j)])
                return

            
            for p in generate(0, []):
                if not p:
                    continue
                tmp = list(states)
                for i, j in p:
                    tmp[i] -= 1
                res = min(res, 1+dfs(*tmp))

            return res

        args = [len(x) for x in directions]
        return dfs(*args)




作者：ga-beng-cui-7
链接：https://leetcode-cn.com/problems/Y1VbOX/solution/pan-duan-liang-tiao-lu-jing-shi-fou-hui-naed1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。















from functools import lru_cache


def cut(start, end, x):
    if (start < end and start <= x <= end) or (start > end and not (end < x < start)):
        return -1
    return 1


MOD = 4
valids = set()
for i in range(MOD):
    for j in range(MOD):
        for ii in range(MOD):
            for jj in range(MOD):
                if i == j or ii == jj or i == ii or j == jj:
                    continue
                if cut(i, j, ii)*cut(i, j, jj) == -1:
                    continue
                valids.add((i, j, ii, jj))


class Solution:
    def trafficCommand(self, directions: List[str]) -> int:
        mp = {'E': 0, 'S': 1, 'W': 2, 'N': 3}

        @lru_cache(None)
        def dfs(e, s, w, n):
            if e+s+w+n == 0:
                return 0
            states = [e, s, w, n]
            res = float('inf')

            def generate(i, path):
                if i == 4:
                    yield path
                    return
                yield from generate(i+1, path)
                if states[i] == 0:
                    return
                j = mp[directions[i][-states[i]]]
                cur = (i, j)
                for ii, jj in path:
                    if (i, j, ii, jj) not in valids:
                        return
                yield from generate(i+1, path+[(i, j)])
                return

            
            for p in generate(0, []):
                if not p:
                    continue
                tmp = [e, s, w, n]
                for i, j in p:
                    tmp[i] -= 1
                res = min(res, 1+dfs(tmp[0], tmp[1], tmp[2], tmp[3]))

            return res

        return dfs(len(directions[0]), len(directions[1]), len(directions[2]), len(directions[3]))



# from functools import lru_cache


# def cut(start, end, x):
#     if (start < end and start <= x <= end) or (start > end and not (end < x < start)):
#         return -1
#     return 1


# MOD = 4
# valids = set()
# for i in range(MOD):
#     for j in range(MOD):
#         for ii in range(MOD):
#             for jj in range(MOD):
#                 if i == j or ii == jj or i == ii or j == jj:
#                     continue
#                 if cut(i, j, ii)*cut(i, j, jj) == -1:
#                     continue
#                 valids.add((i, j, ii, jj))


# class Solution:
#     def trafficCommand(self, directions: List[str]) -> int:
#         mp = {'E': 0, 'S': 1, 'W': 2, 'N': 3}

#         @lru_cache(None)
#         def dfs(e, s, w, n):
#             if e+s+w+n == 0:
#                 return 0
#             states = [e, s, w, n]
#             res = float('inf')

#             def generate(i, path, paths):
#                 if i == 4:
#                     paths.append(path)
#                     return
#                 generate(i+1, path, paths)
#                 if states[i] == 0:
#                     return
#                 j = mp[directions[i][-states[i]]]
#                 cur = (i, j)
#                 flag = True
#                 for ii, jj in path:
#                     if (i, j, ii, jj) not in valids:
#                         flag = False
#                         break
#                 if flag:
#                     generate(i+1, path+[(i, j)], paths)
#                 return

#             ps = []
#             generate(0, [], ps)
#             for p in ps:
#                 if not p:
#                     continue
#                 tmp = [e, s, w, n]
#                 for i, j in p:
#                     tmp[i] -= 1
#                 res = min(res, 1+dfs(tmp[0], tmp[1], tmp[2], tmp[3]))

#             return res

#         return dfs(len(directions[0]), len(directions[1]), len(directions[2]), len(directions[3]))



# def cut(start, end, x):
#     if (start < end and start <= x <= end) or (start > end and not (end < x < start)):
#         return -1
#     return 1 


# MOD = 4;
# valids = set()
# for i in range(MOD):
#     for j in range(MOD):
#         for ii in range(MOD):
#             for jj in range(MOD):
#                 if i == j or ii == jj or i == ii or j == jj:
#                     continue
#                 if cut(i,j,ii)*cut(i,j,jj) == -1:
#                     continue
#                 valids.add((i,j,ii,jj))





# from functools import lru_cache
# class Solution:
#     def trafficCommand(self, directions: List[str]) -> int:
#         mp = {'E':0,'S':1,'W':2,'N':3}
#         def check(moves):
#             m = len(moves)
#             for i in range(m):
#                 for j in range(i+1,m):
#                     if (moves[i][0],moves[i][1],moves[j][0],moves[j][1]) not in valids:
#                         return False
#             return True



#         @lru_cache(None)
#         def dfs(e,s,w,n):
#             if e+s+w+n == 0:
#                 return 0
#             states = [e,s,w,n]
#             res = float('inf')
#             for i in range(1,16):
#                 if any(((i>>j)&1) & (states[j] == 0) for j in range(4)):
#                     continue
#                 # print(e,s,w,n)
#                 # print(i,[((i>>j)&1) & (states[j] == 0) for j in range(4)])
#                 moves = []
#                 for j in range(4):
#                     if (i & (1<<j)):
#                         moves.append([j,mp[directions[j][-states[j]]]])
#                 if check(moves):
#                     res = min(res, 1+dfs(e-((i>>0)&1),s-((i>>1)&1),w-((i>>2)&1),n-((i>>3)&1)))
#             return res
        
#         return dfs(len(directions[0]),len(directions[1]), len(directions[2]), len(directions[3]))

