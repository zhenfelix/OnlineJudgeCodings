# class Solution:
#     def maxJumps(self, arr: List[int], d: int) -> int:
#         n = len(arr)
#         dp = [1] * (n + 1)
#         st = []
#         for i, h in enumerate(arr + [float('inf')]):
#             pre, jump = -1, 0
#             while st and arr[st[-1]] < h:
#                 cur = st.pop()
#                 if pre >= 0 and arr[cur] > arr[pre] and pre-cur <= d:
#                     dp[cur] = max(dp[cur], 1 + jump) ###buggy `pre-cur <= d` loose conditions for updating left dp values, value `jump` could come from the place out of reach for `cur` 
#                 pre = cur
#                 jump = max(jump, dp[cur])
#                 if i - cur <= d:
#                     dp[i] = max(dp[i], 1 + jump)
#             st.append(i)
#             # print(st,dp)
#         return max(dp[:-1])


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        arr += [float('inf')]
        dp = [1] * (len(arr))
        st = []
        for i, h in enumerate(arr):
            while st and arr[st[-1]] < h:
                plateau = [st.pop()]
                while st and arr[st[-1]] == arr[plateau[0]] :
                    plateau.append(st.pop())
                for p in plateau:
                    if i-p <= d:
                        dp[i] = max(dp[i], dp[p]+1)
                    if st and p-st[-1] <= d:
                        dp[st[-1]] = max(dp[st[-1]], dp[p]+1)
            st.append(i)
            # print(st,dp)
        return max(dp[:-1])


import functools

class Solution:
    def maxJumps(self, A, d):
        N = len(A)
        graph = collections.defaultdict(list)
        
        def jump(iterator):
            stack = []
            for i in iterator:
                while stack and A[stack[-1]] < A[i]:
                    j = stack.pop()
                    if abs(i - j) <= d: graph[j].append(i)
                stack.append(i)
        
        jump(range(N))
        jump(reversed(range(N)))
        
        @functools.lru_cache(maxsize=None)
        def height(i):
            return 1 + max(map(height, graph[i]), default=0)
        
        return max(map(height, range(N)))


class Solution:
    def query(self,root,left,right,ql,qr):
        if right < ql or left > qr:
            return -float('inf')
        if left >= ql and right <= qr:
            return self.tree[root]
        mid = (left+right)//2
        return max(self.query(root*2+1,left,mid,ql,qr),self.query(root*2+2,mid+1,right,ql,qr))

    def update(self,root,left,right,pos,val):
        if right < pos or left > pos:
            return
        if left == right:
            self.tree[root] = val
            return
        mid = (left+right)//2
        self.update(root*2+1,left,mid,pos,val)
        self.update(root*2+2,mid+1,right,pos,val)
        self.tree[root] = max(self.tree[root*2+1],self.tree[root*2+2])
        return


    def maxJumps(self, A, d):
        n, inf = len(A), float('inf')
        self.tree = [0]*(4*n+10)
        l_bound, r_bound = [i for i in range(n)], [i for i in range(n)]
        st = []
        for i, a in enumerate(A+[inf]):
            while st and A[st[-1]] <= a:
                r_bound[st[-1]] = min(i-1,st[-1]+d)
                st.pop()
            st.append(i)
        st = []
        for i, a in enumerate(A[::-1]+[inf]):
            i = n-1-i
            while st and A[st[-1]] <= a:
                l_bound[st[-1]] = max(i+1,st[-1]-d)
                st.pop()
            st.append(i)

        for i in sorted(range(n), key=lambda x: A[x]):
            pre = 0
            if l_bound[i] < i:
                pre = max(pre, self.query(0,0,n-1,l_bound[i],i-1))
            if i < r_bound[i]:
                pre = max(pre, self.query(0,0,n-1,i+1,r_bound[i]))
            self.update(0,0,n-1,i,pre+1)
        return self.query(0,0,n-1,0,n-1)