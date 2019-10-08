class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        for k in range(n - 1):
            a0 = e + i + u
            e0 = a + i
            i0 = e + o
            o0 = i
            u0 = i + o
            a, e, i, o, u = a0, e0, i0, o0, u0
        return (a + e + i + o + u) % (10**9 + 7)


# class Solution:
#   def countVowelPermutation(self, n: int) -> int:
#     def dfs(ch, idx):
#       if (ch, idx) in memo:
#         return memo[ch,idx]
#       res = 0
#       if idx == n:
#         memo[ch,idx] = 1
#         return 1
#       if ch == 'a':
#         res += dfs('e', idx+1)
#       elif ch == 'e':
#         res += dfs('a', idx+1)
#         res += dfs('i', idx+1)
#       elif ch == 'i':
#         for chr in 'aeou':
#           res += dfs(chr, idx+1)
#       elif ch == 'o':
#         res += dfs('i', idx+1)
#         res += dfs('u', idx+1)
#       else:
#         res += dfs('a', idx+1)
#       res %= mod
#       memo[ch,idx] = res
#       return res

#     memo = {}
#     mod = 10**9 + 7
#     ans = 0
#     for x in 'aeiou':
#       ans += dfs(x, 1)
#       ans %= mod
#     return ans

  
  
  
  
  
  
  