# class Solution:
#     def mctFromLeafValues(self, arr: List[int]) -> int:
#         dp = {}
#         n = len(arr)
#         p = [[0]*n for _ in range(n)]
#         for r in range(n):
#             for c in range(r,n):
#                 if c == r:
#                     p[r][c] = arr[r]
#                 else:
#                     p[r][c] = p[r][c-1]
#                     p[r][c] = max(p[r][c],arr[c])
                        
                    
                    
                    
#         def dfs(i,j):
#             if (i,j) in dp:
#                 return dp[i,j]
#             if i == j:
#                 dp[i,j] = 0
#                 return 0
#             ans = (1<<31)
#             for k in range(i,j):
#                 ans = min(ans,p[i][k]*p[k+1][j]+dfs(i,k)+dfs(k+1,j))
#             dp[i,j] = ans
#             return ans
        
#         return dfs(0,n-1)



# class Solution:
#     def mctFromLeafValues(self, arr: List[int]) -> int:
#         @lru_cache(None)
#         def dfs(i,j):
#             if i == j:
#                 return 0
#             return min(dfs(i,k)+dfs(k+1,j)+max(arr[i:k+1])*max(arr[k+1:j+1]) for k in range(i,j))

#         n = len(arr)
#         return dfs(0,n-1)


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        @lru_cache(None)
        def interval(i,j):
            if i == j:
                return arr[i]
            return max(interval(i,j-1),arr[j])

        @lru_cache(None)
        def dfs(i,j):
            if i == j:
                return 0
            return min(dfs(i,k)+dfs(k+1,j)+interval(i,k)*interval(k+1,j) for k in range(i,j))

        n = len(arr)
        return dfs(0,n-1)


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        n = len(arr)
        L = [i-1 for i in range(n)]
        R = [i+1 for i in range(n)]
        R[-1] = -1
        q = [(x,i) for i, x in enumerate(arr)]
        res = 0
        cnt = 0
        for x, i in sorted(q):
            b = float('inf')
            left = L[i]
            right = R[i]
            if left >= 0:
                b = min(b,arr[left])
                R[left] = right
            if right >= 0:
                b = min(b,arr[right])
                L[right] = left
            res += x*b
            cnt += 1
            if cnt == n-1:
                break
        return res



class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        def dfs(i,j,lmx,rmx):
            if i > j:
                return 0
            k = max(range(i,j+1), key = lambda x : arr[x])
            tmp = arr[k]*min(lmx,rmx)
            tmp = tmp if tmp < float('inf') else 0
            tmp += dfs(i,k-1,lmx,arr[k])
            tmp += dfs(k+1,j,arr[k],rmx)
            print(k,arr[k])
            return tmp
        return dfs(0,len(arr)-1,float('inf'),float('inf'))

class Solution2:
    def mctFromLeafValues(self, arr):
        res = 0
        arr.append(float('inf'))
        st = [-1]
        for i, a in enumerate(arr):
            while st and arr[st[-1]] < a:
                cur = st.pop()
                tmp = arr[cur]*min(arr[st[-1]], a)
                tmp = tmp if tmp < float('inf') else 0
                res += tmp 
                print(cur,arr[cur])
            st.append(i)
        return res




class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        n = len(arr)
        L = [i-1 for i in range(n)]
        R = [i+1 for i in range(n)]
        R[-1] = -1
        removed = [0]*n
        q = [(arr[i]*arr[i+1],i,i+1) for i in range(n-1)]
        heapq.heapify(q)
        cnt = 0
        res = 0
        while q:
            val, i, j = heapq.heappop(q)
            if removed[i] or removed[j]:
                continue
            # print(val,i,j)
            res += val
            if arr[j] < arr[i]:
                i = j
            removed[i] = 1
            left, right = L[i], R[i]
            if left >= 0:
                R[left] = right
            if right >= 0:
                L[right] = left
            cnt += 1
            if left >= 0 and right >= 0:
                heapq.heappush(q,(arr[left]*arr[right],left,right))
            if cnt == n-1:
                break
        return res


        

class Solution:
    def mctFromLeafValues(self, A):
        res, n = 0, len(A)
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack)  >2:
            res += stack.pop() * stack[-1]
        return res
        