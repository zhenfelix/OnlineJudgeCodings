# proof: https://leetcode-cn.com/problems/minimum-jumps-to-reach-home/solution/dao-jia-de-zui-shao-tiao-yue-ci-shu-zui-duan-lu-zh/


# class Solution:
#     def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
#         forbidden =set([(p,True) for p in forbidden]+[(p,False) for p in forbidden])
#         q = deque()
#         q.append((0,True,0))
#         forbidden.add((0,True))
#         while q:
#             pos, right, cnt = q.popleft()
#             if pos == x:
#                 return cnt
#             if (pos+a,True) not in forbidden:
#                 q.append((pos+a,True,cnt+1))
#                 forbidden.add((pos+a,True))
#             if right and pos-b > 0 and (pos-b,False) not in forbidden:
#                 q.append((pos-b,False,cnt+1))
#                 forbidden.add((pos-b,False))
#         return -1

# class Solution:
#     def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
#         forbidden =set([(p,1) for p in forbidden]+[(p,2) for p in forbidden])
#         # reach = max(max(forbidden),x)+a+b 
#         a, b = a, a-b
#         # def gcd(p,q):
#         #     if p < q:
#         #         p, q = q, p 
#         #     if q == 0:
#         #         return p 
#         #     return gcd(q,p%q)

#         # if b < 0:
#         #     c = gcd(a,-b)
#         #     reach += a*(-b)//c 
#         reach = 6000
#         q = [(0,0)]
#         while q:
#             cnt, pos = heapq.heappop(q)
#             # print(cnt,pos)
#             if pos == x:
#                 return cnt
#             for inc, cost in [(a,1),(b,2)]:
#                 if (pos+inc,cost) in forbidden or not (0 <= pos+inc <= reach):
#                     break
#                 heapq.heappush(q,(cnt+cost,pos+inc))
#                 forbidden.add((pos+inc,cost))
#         return -1

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        Q = deque()
        Q.append((0, 0, False))
        while Q:
            cur, cnt, used = Q.popleft()
            if cur == x:
                # 第一次到x即最小步数，因为队列后序元素cnt都是大于等于当前cnt的
                return cnt
            if cur + a < 6000 and cur + a not in forbidden:
                # 6000是往右探索的最大值，x最大为2000
                forbidden.add(cur+a)
                Q.append((cur+a, cnt+1, False))
            if not used and cur - b > 0 and cur - b not in forbidden:
                # forbidden.add(cur-b) 
                # 这里不能forbidden，因为后退回cur-b处时，无法覆盖前进到cur-b再后退到cur-2b的情况。
                Q.append((cur-b, cnt+1, True))
        return -1


# 作者：captaintec
# 链接：https://leetcode-cn.com/problems/minimum-jumps-to-reach-home/solution/python3-bfs-he-dfsjie-fa-by-captaintec/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。