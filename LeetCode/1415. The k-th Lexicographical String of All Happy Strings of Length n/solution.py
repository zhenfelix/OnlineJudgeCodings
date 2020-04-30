# class Solution:
#     def getHappyString(self, n: int, k: int) -> str:
#         self.n, self.k = n, k
#         self.res, self.kth = "", 1
#         self.dfs("#",0)
#         return self.res

#     def dfs(self,cur,idx):
#         if self.kth > self.k:
#             return
#         if idx == self.n:
#             if self.kth == self.k:
#                 self.res = cur[1:]
#             self.kth += 1
#             return
#         for ch in "abc":
#             if ch != cur[-1]:
#                 self.dfs(cur+ch,idx+1)
#         return


                
class Solution(object):
    def getHappyString(self, n, k):
        # # [!] Brute force, base3 variant
        # for x in range(3 ** n):
        #     # convert x to base 3 sequence
        #     cand = []
        #     for _ in range(n):
        #         if cand and x % 3 == cand[-1]:
        #             break
        #         cand.append(x % 3)
        #         x //= 3
        #     else:
        #         # didn't fail at building the string
        #         k -= 1
        #         if k == 0:
        #             return "".join('abc'[r] for r in cand)[::-1]
        # return ""
        
        # # [!] Brute force, itertools.product variant
        # for cand in itertools.product('abc', repeat=n):
        #     if any(cand[i] == cand[i+1] for i in range(len(cand) - 1)):
        #         continue
        #     k -= 1
        #     if k == 0:
        #         return "".join(cand)
        # return ""
        
        # [!] Backtracking
        ans = [""]
        path = []
        self.k = k
        def search(i):
            if self.k < 0:
                return
            if i == n:
                self.k -= 1
                if self.k == 0:
                    ans.append("".join(path))
                return
            for c in 'abc':
                if not path or path[-1] != c:
                    path.append(c)
                    search(i + 1)
                    path.pop()
        search(0)
        return ans[-1]