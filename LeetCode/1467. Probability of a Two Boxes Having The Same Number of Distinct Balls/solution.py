from functools import lru_cache
class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls)//2
        v = []
        for i, b in enumerate(balls):
            v += [i]*b        

        @lru_cache(None)
        def dfs(idx, box1, box2, cnt1):
            # print(idx, box1, box2, cnt1)
            if cnt1 > n or idx-cnt1 > n:
                return 0, 0
            # if (idx,box1,box2) in memo:
            #     return memo[idx,box1,box2]
            if idx == 2*n:
                cc1, cc2 = 0, 0
                while box1:
                    cc1 += 1
                    box1 = box1 & (box1-1)
                while box2:
                    cc2 += 1
                    box2 = box2 & (box2-1)
                if cc1 == cc2:
                    return 1, 1
                else:
                    return 0, 1
            ball = v[idx]
            a1, b1 = dfs(idx+1, box1|(1<<ball), box2, cnt1+1)
            a2, b2 = dfs(idx+1, box1, box2|(1<<ball), cnt1)
            # memo[idx,box1,box2] = (a1+a2, b1+b2)
            return a1+a2, b1+b2 
            
            
        rr, cc = dfs(0,0,0,0)
        print(rr,cc)
        return rr/cc




# https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/discuss/661992/Python-O(n*k*max(balls))-dfs-with-memory-76ms
from functools import lru_cache
# from math import comb

@lru_cache(None)
def combo(n, k):
    if k==0 or n==k:
        return 1
    return combo(n-1, k) + combo(n-1, k-1)

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        self.n = sum(balls) // 2
        self.balls = balls
        self.k = len(balls)
        return self.dfs(0, 0, 0, 0, 0)
        
    # def com(self, n, m):
    #     ans = 1
    #     for i in range(n-m+1, n+1):
    #         ans *= i
    #     for i in range(1, m+1):
    #         ans //= i
    #     return ans
        
    @lru_cache(None)
    def dfs(self, left, right, i, ul, ur):
        if left > self.n or right > self.n or ul > ur+self.k-i or ur > ul+self.k-i:
            return 0
        if i == len(self.balls):
            return float(ul == ur)
        p = 0
        for l in range(self.balls[i]+1):
            r = self.balls[i] - l
            if left+l > self.n or r+right > self.n:
                continue
            p += combo(self.n-left, l) * combo(self.n-right, r) / combo(2*self.n-left-right, self.balls[i]) * self.dfs(left+l, right+r, i+1, ul+(l>0), ur+(r>0))
        return p



# class Solution:
#     def getProbability(self, balls: List[int]) -> float:
#         from math import factorial
        
#         firstHalf = {}
#         secondHalf = {}
        
#         # successful permutations
#         self.good = 0
#         # total number of valid permutations
#         self.all = 0
#         def dfs(i):
#             if i == len(balls):
#                 s1 = sum(firstHalf.values())
#                 s2 = sum(secondHalf.values())
#                 # invalid permutation if the total number of balls in each
#                 # half is not equal, because we only consider permutations
#                 # with equal balls in each half
#                 if s1 != s2:
#                     return 0
                
#                 # Get the number of permutations in the FIRST HALF of the result array.
#               # If you don't understand, search "geeks for geeks number of distinct permutations" on Google.
#                 prod1 = 1
#                 for k in firstHalf:
#                     prod1 *= factorial(firstHalf[k])
#                 p1 = factorial(s1) / prod1
                
#                 # Same as above but for the SECOND HALF of the array.
#                 prod2 = 1
#                 for k in secondHalf:
#                     prod2 *= factorial(secondHalf[k])
#                 p2 = factorial(s2) / prod2
                
#                 # We can use each permutation as many times as possible since the problem
#                 # tells us they're all unique regardless of order. So [1, 2 / 1, 3] is separate
#                 # from [2, 1 / 3, 1].
#                 self.all += p1 * p2
#                 # only add to the "successful" permutations if we meet our success criteria: equal number 
#                 # of unique balls in each half of the array.
#                 self.good += p1 * p2 if len(firstHalf) == len(secondHalf) else 0
#             else:
#                 # This will calculate every permutation of splitting the number of balls of color i
#                 # into each half. We So if there are 3 balls of color i, the iterations will split like this,
#                 # in order:
#                 # 0 -> first: 3, second: 0
#                 # 1 -> first: 2, second: 1
#                 # 2 -> first: 1, second: 2
#                 # 3 -> first: 0, second: 3
#                 firstHalf[i] = balls[i]
#                 for _ in range(((balls[i])) + 1):
#                     dfs(i + 1)
                    
#                     if i in firstHalf:
#                         firstHalf[i] -= 1
#                         if firstHalf[i] == 0:
#                             del firstHalf[i]
#                     secondHalf[i] = secondHalf.get(i, 0) + 1
                    
#                 del secondHalf[i]
                
#         dfs(0)
#         # print(self.good, self.all)
#         # if we have X good permutations and Y total permutations, the odds that a randomly
#         # selected permutation will be "good" is X / Y AS LONG AS each permutation is equally likely.
#         return self.good / self.all

# class Solution:
#     def getProbability(self, balls: List[int]) -> float:
#         # from math import factorial
#         k = len(balls)
#         n = sum(balls)//2
#         arr1, arr2 = [0]*k, [0]*k
#         fac = [1]*(n+1)
#         for i in range(n):
#             fac[i+1] = fac[i]*(i+1)

#         def perm(arr):
#             p = 1
#             for a in arr:
#                 p *= fac[a]
#             return fac[n]//p


#         # successful permutations
#         self.good = 0
#         # total number of valid permutations
#         self.all = 0
#         def dfs(i,arr1,arr2,sa1,sa2):
#             if sa1 > n or sa2 > n:
#                 return
#             if i == len(balls):
#                 # print(i,arr1,arr2,sa1,sa2)
#                 s1 = sum(1 for a in arr1 if a > 0)
#                 s2 = sum(1 for a in arr2 if a > 0)
#                 p1 = perm(arr1)
#                 p2 = perm(arr2)
#                 self.all += p1 * p2
#                 self.good += p1 * p2 if s1 == s2 else 0
#                 return
#             for j in range(balls[i]+1):
#                 arr1[i] += j
#                 arr2[i] += balls[i]-j
#                 dfs(i+1,arr1,arr2,sa1+j,sa2+balls[i]-j)
#                 arr2[i] -= balls[i]-j
#                 arr1[i] -= j
#             return
            
            
#         dfs(0,arr1,arr2,0,0)
#         print(self.good, self.all)
#         return self.good / self.all

class Solution:
    def multinomial(self, n):
        return factorial(sum(n))/prod([factorial(i) for i in n])
  
    def getProbability(self, balls):
        # print(self.multinomial([1,2,3]))
        k, n, Q = len(balls), sum(balls)// 2, 0
        left = [range(0,i+1) for i in balls]
        right = [range(i,-1,-1) for i in balls]
        # t = list(product(*arrays))
        left = product(*left)
        right = product(*right)
        for i, j in zip(left,right):
            if sum(i) == n and i.count(0) == j.count(0):
                Q += self.multinomial(i) * self.multinomial(j) 
                
        print(Q)
        return Q / self.multinomial(list(balls))


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls)//2
        k = len(balls)
        cnt, res = 0, 0
        def dfs(path):
            # print(path)
            nonlocal res, cnt
            if len(path) == 2*n:
                cnt += 1
                if len(set(path[:n])) == len(set(path[n:])):
                    res += 1
                return
            for i in range(k):
                if path and path[-1] == i:
                    continue
                if balls[i] > 0:
                    tmp = []
                    total = balls[i]
                    for j in range(1,total+1):
                        tmp += [i]
                        balls[i] -= j
                        dfs(path+tmp)
                        balls[i] += j
            return
            
        dfs([])
        print(res,cnt)
        return res/cnt