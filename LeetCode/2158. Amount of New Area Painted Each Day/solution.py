class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        n = len(paint)
        lines = []
        for i, se in enumerate(paint):
            lines.append((se[0],1,i))
            lines.append((se[1],-1,i))
        lines.sort()
        # print(lines)
        ans = [0]*n 
        pre, pi = -1, n
        hq = [n]
        closed = [False]*(n+1)
        for cur, delta, i in lines:
            # print(hq,pre,cur)
            pi = hq[0]
            if pi < n:
                ans[pi] += cur-pre
            if delta > 0:
                heapq.heappush(hq,i)
            else:
                closed[i] = True
                while hq and closed[hq[0]]:
                    heapq.heappop(hq)
            
            pre = cur 
        return ans 






class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        n = len(paint)
        lines = []
        for i, se in enumerate(paint):
            lines.append(se[0])
            lines.append(se[1])
        lines = sorted(set(lines))
        arr = []
        mp = dict()
        for a, b in zip(lines[:-1],lines[1:]):
            mp[a] = len(arr)
            arr.append(b-a)
        mp[lines[-1]] = len(arr)
        m = len(arr)
        tree = [0]*(4*m)
        lazy = [-1]*(4*m)
        ans = []
        # print(arr,mp)
        def push(idx, lo, hi):
            if lazy[idx] != -1:
                tree[idx] = lazy[idx]
                if lo < hi:
                    lazy[idx*2+1] = lazy[idx]
                    lazy[idx*2+2] = lazy[idx]
                lazy[idx] = -1

        def update(idx, lo, hi, left, right, val):
            # print(idx, lo, hi, left, right, val)
            push(idx, lo, hi)
            if hi < left or lo > right:
                return
            if lo >= left and hi <= right:
                lazy[idx] = val
                push(idx, lo, hi)
                return
            mid = (lo+hi)//2
            update(idx*2+1, lo, mid, left, right, val)
            update(idx*2+2, mid+1, hi, left, right, val)
            tree[idx] = tree[idx*2+1]+tree[idx*2+2]
            return

        def query(idx, lo, hi, left, right):
            push(idx, lo, hi)
            if hi < left or lo > right:
                return 0
            if lo >= left and hi <= right:
                return tree[idx]
            mid = (lo+hi)//2
            cnt = 0
            cnt += query(idx*2+1, lo, mid, left, right)
            cnt += query(idx*2+2, mid+1, hi, left, right)
            return cnt

        for i, v in enumerate(arr):
            update(0, 0, m-1, i, i, v)
        # for i in range(m):
        #     print(query(0, 0, m-1, i, i))
        
        for s, e in paint:
            left, right = mp[s], mp[e]-1
            ans.append(query(0, 0, m-1, left, right))
            update(0, 0, m-1, left, right, 0)

        return ans