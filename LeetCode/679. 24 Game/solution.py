class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def gcd(a,b):
            if b == 0:
                return a if a != 0 else 1
            return gcd(b,a%b)
        def add(l,r):
            la, lb = l 
            ra, rb = r  
            b = lb*rb
            a = la*rb+ra*lb
            c = gcd(a,b)
            return (a//c, b//c)
        def minus(l,r):
            la, lb = l 
            ra, rb = r  
            b = lb*rb
            a = la*rb-ra*lb
            c = gcd(a,b)
            return (a//c, b//c)
        def multiply(l,r):
            la, lb = l 
            ra, rb = r  
            b = lb*rb
            a = la*ra
            c = gcd(a,b)
            return (a//c, b//c)
        def divide(l,r):
            la, lb = l 
            ra, rb = r  
            b = lb*ra
            a = la*rb
            c = gcd(a,b)
            return (a//c, b//c)

        def dfs(path):
            if len(path) == 1:
                return path[-1] == (24,1)
            n = len(path)
            for i in range(n):
                for j in range(i+1,n):
                    npath = [path[k] for k in range(n) if k != i and k != j]
                    x = add(path[i],path[j])
                    if dfs([x]+npath):
                        return True
                    x = minus(path[i],path[j])
                    if dfs([x]+npath):
                        return True
                    x = minus(path[j],path[i])
                    if dfs([x]+npath):
                        return True
                    x = multiply(path[i],path[j])
                    if dfs([x]+npath):
                        return True
                    x = divide(path[i],path[j])
                    if dfs([x]+npath):
                        return True
                    x = divide(path[j],path[i])
                    if dfs([x]+npath):
                        return True
            return False

        return dfs([(x,1) for x in cards])

















class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        mp = {1<<i: i for i in range(4)}
        def gcd(a,b):
            if b == 0:
                return a if a != 0 else 1
            return gcd(b,a%b)
        def add(l,r):
            la, lb = l 
            ra, rb = r  
            b = lb*rb
            a = la*rb+ra*lb
            c = gcd(a,b)
            return (a//c, b//c)
        def minus(l,r):
            la, lb = l 
            ra, rb = r  
            b = lb*rb
            a = la*rb-ra*lb
            c = gcd(a,b)
            return (a//c, b//c)
        def multiply(l,r):
            la, lb = l 
            ra, rb = r  
            b = lb*rb
            a = la*ra
            c = gcd(a,b)
            return (a//c, b//c)
        def divide(l,r):
            la, lb = l 
            ra, rb = r  
            b = lb*ra
            a = la*rb
            c = gcd(a,b)
            return (a//c, b//c)

        @lru_cache(None)
        def dfs(state):
            if state in mp:
                return {(cards[mp[state]],1)}
            candidates = set()
            cur = state
            while cur:
                if cur and state-cur:
                    left = dfs(cur)
                    right = dfs(state-cur)
                    for l in left:
                        for r in right:
                            lr = add(l,r)
                            candidates.add(lr)
                            lr = minus(l,r)
                            candidates.add(lr)
                            lr = minus(r,l)
                            candidates.add(lr)
                            lr = multiply(l,r)
                            candidates.add(lr)
                            lr = divide(l,r)
                            candidates.add(lr)
                            lr = divide(r,l)
                            candidates.add(lr)
                                
                cur = (cur-1)&state
            # print(i,j,candidates)
            return candidates
        # print(len(dfs((1<<4)-1)))
        return (24,1) in dfs((1<<4)-1)







import itertools
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        
        def dfs(i, j):
            if (i,j) in memo:
                return memo[i,j]
            if i == j:
                memo[i,j] = [(nums_[i],1)]
                return memo[i,j]
            memo[i,j] = []
            for k in range(i+1,j+1):
                left, right = dfs(i,k-1), dfs(k,j)
                memo[i,j] += [(l[0]*r[0],l[1]*r[1]) for l in left for r in right]
                memo[i,j] += [(l[0]*r[1],l[1]*r[0]) for l in left for r in right]
                memo[i,j] += [(l[0]*r[1]+r[0]*l[1],l[1]*r[1]) for l in left for r in right]
                memo[i,j] += [(l[0]*r[1]-r[0]*l[1],l[1]*r[1]) for l in left for r in right]
            return memo[i,j]


        p = itertools.permutations(nums)
        for nums_ in p:
            # print(nums_)
            memo = {}
            dfs(0,3)
            # print(memo[0,3])
            for p, q in memo[0,3]:
                if q != 0 and 24 * q == p:
                    # print(p,q)
                    return True

        return False


