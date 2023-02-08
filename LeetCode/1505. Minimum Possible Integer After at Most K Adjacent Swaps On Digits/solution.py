class Solution:
    def minInteger(self, num: str, k: int) -> str:
        def query(pos, arr):
            cnt = 0
            while pos:
                cnt += arr[pos]
                pos -= pos&(-pos)
            return cnt
        def update(pos, v, arr):
            m = len(arr)
            while pos < m:
                arr[pos] += v 
                pos += pos&(-pos)
            return 

        mp = defaultdict(deque)
        for i, ch in enumerate(num):
            mp[ch].append(i)
        n = len(num)
        tree = [0]*(n+5)
        for i in range(n):
            update(i+1,1,tree)
        ans = []
        for _ in range(n):
            for ch in digits:
                if mp[ch]:
                    i = mp[ch][0]
                    cnt = query(i,tree)
                    # print(ch,i,cnt)
                    if cnt <= k:
                        k -= cnt
                        ans.append(ch)
                        update(i+1,-1,tree)
                        mp[ch].popleft()
                        break

        return ''.join(ans)


# class Solution:
#     def minInteger(self, num: str, k: int) -> str:
#         n = len(num)
#         mp = defaultdict(deque)
#         for i,v in enumerate(num):
#             mp[v].append(i)
#         res = ""
#         def lowbit(x):
#             return x & (-x)
#         def query(x):
#             sums = 0
#             while x:
#                 sums += arr[x]
#                 x -= lowbit(x)
#             return sums
#         def update(x,delta):
#             while x <= n:
#                 arr[x] += delta
#                 x += lowbit(x)

#         arr = [0]*(n+1)
#         for i in range(n):
#             update(i+1,1)

#         for i in range(n):
#             for v in "0123456789":
#                 if mp[v] and query(mp[v][0]) <= k:
#                     idx = mp[v].popleft()
#                     k -= query(idx)
#                     res += v
#                     update(idx+1,-1)
#                     break
#         return res


# from collections import defaultdict, deque
# from sortedcontainers import SortedList
# from string import digits
# class Solution:
#     def minInteger(self, num: str, k: int) -> str:
#         d = defaultdict(deque)
#         for i, a in enumerate(num):
#             d[a].append(i)
#         ans, seen = '', SortedList()
#         for _ in range(len(num)):
#             for a in digits:
#                 if d[a]:
#                     i = d[a][0]
#                     ni = i + (len(seen) - seen.bisect(i))
#                     dis = ni - len(seen)
#                     if dis <= k:
#                         k -= dis
#                         d[a].popleft()
#                         ans += a
#                         seen.add(i)
#                         break
#         return ans


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        digits = defaultdict(deque)
        for i, c in enumerate(num):
            digits[c].append(i)
        ret, moved = '', []
        for _ in range(len(num)):
            for c in string.digits:
                if digits[c]:
                    idx = digits[c][0]
                    real_idx = idx - bisect.bisect(moved, idx)
                    if real_idx <= k:
                        k -= real_idx
                        ret += c
                        bisect.insort(moved, digits[c].popleft())
                        break
        return ret
