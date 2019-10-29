
# class Solution:
    # def isNStraightHand(self, hand: List[int], W: int) -> bool:
    #     hand.sort()
    #     q = collections.deque()
    #     # print(hand)
    #     for h in hand:
    #         # print(q)
    #         if q:
    #             idx = 0
    #             while idx < len(q) and q[idx][-1] == h:
    #                 idx += 1
    #             if idx == len(q):
    #                 q.append([h])
    #             elif q[idx][-1]+1 < h:
    #                 return False
    #             else:
    #                 q[idx].append(h)                
    #         else:
    #             q.append([h])
    #         while q and len(q[0]) == W:
    #             q.popleft()
    #     if q:
    #         return False
    #     return True
    
    # def isNStraightHand(self, hand, W):
    #     c = collections.Counter(hand)
    #     for i in sorted(c):
    #         # print(c)
    #         if c[i] > 0:
    #             for j in range(W)[::-1]:
    #                 c[i + j] -= c[i]
    #                 if c[i + j] < 0:
    #                     return False
    #     return True

    

# class Solution:
#     def isNStraightHand(self, hand: List[int], W: int) -> bool:
#         cnt = collections.Counter(hand)
#         # print(hand)
#         while cnt:
#             cur = min(cnt)
#             for nxt in range(cur,cur+W)[::-1]:
#                 cnt[nxt] -= cnt[cur]
#                 if cnt[nxt] < 0:
#                     return False
#                 elif cnt[nxt] == 0:
#                     del cnt[nxt]
#         return True

class Solution:
    def isNStraightHand(self, hand, W):
        c = collections.Counter(hand)
        start = collections.deque()
        last_checked, opened = -1, 0
        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last_checked + 1: return False
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == W: opened -= start.popleft()
        return opened == 0

