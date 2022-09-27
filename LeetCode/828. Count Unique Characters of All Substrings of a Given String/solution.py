# class Solution:
#     def uniqueLetterString(self, s: str) -> int:
#         zeros, ones = [0]*26, [0]*26
#         MOD = 10**9+7
#         res = 0
#         for ch in s:
#             cur = ord(ch) - ord('A')
#             for i in range(26):
#                 if i == cur:
#                     ones[i] = zeros[i] + 1
#                     zeros[i] = 0
#                 else:
#                     zeros[i] += 1
#             res += sum(ones)
#             res %= MOD

#         return res

# class Solution:
#     def uniqueLetterString(self, s: str) -> int:
#         zeros, ones = [0]*26, [0]*26
#         MOD = 10**9+7
#         res, sums, total = 0, 0, 0
#         for ch in s:
#             cur = ord(ch) - ord('A')
#             total += 1
#             sums -= ones[cur]
#             ones[cur] = total - zeros[cur]
#             sums += ones[cur]
#             zeros[cur] = total 
#             sums %= MOD
#             res += sums
#             res %= MOD

#         return res

class Solution:
#     def uniqueLetterString(self, s: str) -> int:
#         MOD = 10**9+7
#         pos = [0]*26
#         mp = [[-1] for _ in range(26)]
#         n, res = len(s), 0
#         for i, ch in enumerate(s):
#             cur = ord(ch) - ord('A')
#             mp[cur].append(i)
#         for j in range(26):
#             mp[j].append(n)
#         for i, ch in enumerate(s):
#             cur = ord(ch) - ord('A')
#             pos[cur] += 1
#             idx = pos[cur]
#             res += (mp[cur][idx]-mp[cur][idx-1])*(mp[cur][idx+1]-mp[cur][idx])
#             res %= MOD

#         return res

    def uniqueLetterString(self, S):
        index = {c: [-1, -1] for c in string.ascii_uppercase}
        res = 0
        for i, c in enumerate(S):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            res += (len(S) - j) * (j - k)
        return res % (10**9 + 7)


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        mp = [[-1] for _ in range(26)]
        for i, ch in enumerate(s):
            ch = ord(ch)-ord('A')
            mp[ch].append(i)
        ans = 0
        for i in range(26):
            mp[i].append(n)
            m = len(mp[i])
            for j in range(1,m-1):
                ans += (mp[i][j]-mp[i][j-1])*(mp[i][j+1]-mp[i][j])
        return ans 