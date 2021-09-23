class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def counter(s, start, last, count, left): #count increase from start
            if left < 0:
                return float('inf')
            if start >= len(s):
                return 0
            if s[start] == last:
                incr = 1 if count == 1 or count == 9 or count == 99 else 0
                return incr + counter(s, start+1, last, count+1, left) # we keep it
                # return min(incr + counter(s, start+1, last, count+1, left), counter(s, start + 1, last, count, left - 1)) # we keep it or not
            else:
				# keep it or delete it
                return min(1 + counter(s, start+1, s[start], 1, left), counter(s, start + 1, last, count, left - 1))
            
        return counter(s, 0, "", 0, k)



class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        memo = {}
        
        cost = [0] * 111
        cost[1] = 1
        for i in range(2, len(cost)):
            cost[i] = len(f"a{i}")
            
        def f(i, k, right_ch, cnt):
            if (i, k, right_ch, cnt) in memo:
                return memo[i, k, right_ch, cnt]
            if i < 0:
                return cost[cnt]
            ans = 1 << 29
            # Not delete
            if s[i] == right_ch:
                ans = min(ans, f(i-1, k, right_ch, cnt+1))
            else:
                ans = min(ans, f(i-1, k, s[i], 1) + cost[cnt])
            
            # Delete
            if k > 0:
                ans = min(ans, f(i-1, k-1, right_ch, cnt))
                
            memo[i, k, right_ch, cnt] = ans
            return ans
        
        return f(len(s) - 1, k, 'a', 0)



# from functools import lru_cache
# class Solution:
#     def getLengthOfOptimalCompression(self, s: str, K: int) -> int:
#         def compress(ss):
#             # print(ss)
#             n = len(ss)
#             st = [ss[0]]
#             cnt = 1
#             for i in range(1,n):
#                 if ss[i] != ss[i-1]:
#                     if cnt > 1:
#                         st.append(str(cnt))
#                     st.append(ss[i])
#                     cnt = 1
#                 else:
#                     cnt += 1
#             if cnt > 1:
#                 st.append(str(cnt))
#             # print(st)
#             return ''.join(st)



#         @lru_cache(None)
#         def dfs(i,k,alpha,last):
#             res = float('inf')

#             if k <= 0 and i >= 0:
#                 if alpha != s[i]:
#                     return res
#                 j, cnt = i, 0
#                 while j >= 0 and s[j] == alpha:
#                     j -= 1
#                     cnt += 1
#                 if cnt == last:
#                     res = len(compress(s[:i+1]))
#             elif k >= i+1 or i < 0:
#                 if alpha == chr(ord('a')+26):
#                     res = 0
#             elif last > cc[i][alpha]:
#                 return res
#             else:
#                 if s[i] == alpha:
#                     for idx in range(27):
#                         ch = chr(ord('a')+idx)
#                         if ch == alpha and last > 1:
#                             tmp = dfs(i-1,k,ch,last-1)
#                             if last == 2:
#                                 tmp += 1
#                             res = min(res, tmp+len(str(last))-len(str(last-1)))
#                         elif last == 1:
#                             for d in range(1,i+1):
#                                 res = min(res,dfs(i-1,k,ch,d)+1)
#                 res = min(res,dfs(i-1,k-1,alpha,last))
#             # if res != float('inf'): print(i,k,alpha,last,res)
#             # print(i,k,alpha,last,res)
#             return res
#         n = len(s)
#         cc = []
#         for i in range(n):
#             cc.append(Counter(s[:i+1]))
#         return min(dfs(n-1,K,chr(ord('a')+ch),d) for ch in range(27) for d in range(1,len(s)+1))
