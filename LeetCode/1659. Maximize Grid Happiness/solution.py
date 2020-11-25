# from functools import lru_cache


# class Solution:
#     def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
#         @lru_cache(None)
#         def dfs(occupy, choice, row, intro, extro):
#             # print(occupy, choice, row, intro, extro)
#             if row == m:
#                 return 0
#             res = 0
#             for occupy_cur in range(1 << n):
#                 choice_cur = occupy_cur
#                 while 1:
#                     # for choice_cur in range(1<<n):
#                     intro_mask_cur, extro_mask_cur = occupy_cur & (
#                         ~choice_cur), occupy_cur & choice_cur
#                     intro_mask, extro_mask = occupy & (
#                         ~choice), occupy & choice
#                     intro_cur = intro - bin(intro_mask_cur).count('1')
#                     extro_cur = extro - bin(extro_mask_cur).count('1')
#                     if intro_cur >= 0 and extro_cur >= 0:
#                         cur = bin(intro_mask_cur).count('1')*120 + \
#                             bin(extro_mask_cur).count('1')*40
#                         cur -= bin(intro_mask_cur &
#                                    (occupy_cur >> 1)).count('1')*30
#                         cur -= bin(intro_mask_cur &
#                                    (occupy_cur << 1)).count('1')*30
#                         cur -= bin(intro_mask_cur & occupy).count('1')*30
#                         cur += bin(extro_mask_cur &
#                                    (occupy_cur >> 1)).count('1')*20
#                         cur += bin(extro_mask_cur &
#                                    (occupy_cur << 1)).count('1')*20
#                         cur += bin(extro_mask_cur & occupy).count('1')*20
#                         cur -= bin(intro_mask & occupy_cur).count('1')*30
#                         cur += bin(extro_mask & occupy_cur).count('1')*20
#                         cur += dfs(occupy_cur, choice_cur,
#                                    row+1, intro_cur, extro_cur)
#                         res = max(res, cur)
#                     # print(occupy_cur, choice_cur)
#                     if choice_cur == 0:
#                         break
#                     choice_cur = (choice_cur-1) & occupy_cur

#             return res

#         return dfs(0, 0, 0, introvertsCount, extrovertsCount)

from functools import lru_cache


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        @lru_cache(None)
        def dfs(occupy, choice, i, j, intro, extro):
            # print(occupy, choice, row, intro, extro)
            if j == n:
                return dfs(occupy,choice,i+1,0,intro,extro)
            if i == m:
                return 0
            res = dfs(occupy>>1,choice>>1,i,j+1,intro,extro)
            if intro > 0:
                c1 = dfs((occupy>>1)|(1<<(n-1)),choice>>1,i,j+1,intro-1,extro) + 120
                if occupy&1:
                    c1 -= 30
                    if choice&1:
                        c1 += 20
                    else:
                        c1 -= 30
                if j > 0 and occupy&(1<<(n-1)):
                    c1 -= 30
                    if choice&(1<<(n-1)):
                        c1 += 20
                    else:
                        c1 -= 30
                res = max(res,c1)
            if extro > 0:
                c2 = dfs((occupy>>1)|(1<<(n-1)),(choice>>1)|(1<<(n-1)),i,j+1,intro,extro-1) + 40
                if occupy&1:
                    c2 += 20
                    if choice&1:
                        c2 += 20
                    else:
                        c2 -= 30
                if j > 0 and occupy&(1<<(n-1)):
                    c2 += 20
                    if choice&(1<<(n-1)):
                        c2 += 20
                    else:
                        c2 -= 30
                res = max(res,c2)

            return res

        return dfs(0, 0, 0, 0, introvertsCount, extrovertsCount)


class Solution:
    def getMaxGridHappiness(self, m, n, I, E):
        InG, ExG, InL, ExL = 120, 40, -30, 20
        fine = [[0, 0, 0], [0, 2*InL, InL+ExL], [0, InL+ExL, 2*ExL]]
        
        @lru_cache(None)
        def dp(index, row, I, E):
            if index == -1: return 0

            R, C, ans = index//n, index%n, []
            neibs = [(1, I-1, E, InG), (2, I, E-1, ExG), (0, I, E, 0)]  
            
            for val, dx, dy, gain in neibs:
                tmp = 0
                if dx >= 0 and dy >= 0:
                    tmp = dp(index-1, (val,) + row[:-1], dx, dy) + gain
                    if C < n-1: tmp += fine[val][row[0]]  #right neighbor
                    if R < m-1: tmp += fine[val][row[-1]] #down neighbor
                ans.append(tmp)

            return max(ans)
        
        if m < n: m, n = n, m
            
        return dp(m*n-1, tuple([0]*n), I, E)