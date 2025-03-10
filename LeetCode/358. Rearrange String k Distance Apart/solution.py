class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        
        n = len(s)
        cc = Counter(s)
        arr = sorted([(cnt,ch) for ch, cnt in cc.items()])
        mx = arr[-1][0]
        if k <= 1 or mx == 1:
            return s
        ans = [[] for _ in range(mx)]
        cur = 0
        for cnt, ch in arr[::-1]:
            for _ in range(cnt):
                if cnt == mx and cur >= mx:
                    cur = 0
                if cnt != mx and cur >= mx-1:
                    cur = 0
                ans[cur].append(ch)
                cur += 1
        # print(ans)
        if len(ans[-2]) >= k:
            return ''.join([''.join(s) for s in ans])

        return ""


# WA Solution
# from collections import Counter, deque
# import heapq

# class Solution:
#     def rearrangeString(self, s: str, k: int) -> str:
#         mp = Counter()
#         n = len(s)
#         for ch in s:
#             mp[ch] += 1
#         arr = [[-a[1],a[0]] for a in mp.items()]
#         heapq.heapify(arr)
#         ans = ''
#         idx = 0
#         q = deque()
#         for i in range(k):
#             q.append(None)
            
#         for i in range(n):
#             if not arr:
#                 return ''
#             tmp = heapq.heappop(arr)
#             ans += tmp[1]
#             tmp[0] += 1
#             if tmp[0] < 0:
#                 q.append(tmp.copy())
#             else:
#                 q.append(None)
#             tmp = q.popleft()
#             if tmp:
#                 heapq.heappush(arr, tmp.copy())

#         return ans
