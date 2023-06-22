class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(nums1), len(queries)
        qs = list(range(m))
        qs.sort(key = lambda x: (-queries[x][0],-queries[x][1]))

        def query(i, tree):
            mx = -1
            while i:
                mx = max(mx, tree[i])
                i -= i&(-i)
            return mx 
        def update(i, v, tree):
            while i < len(tree):
                tree[i] = max(tree[i], v)
                i += i&(-i)
            return

        arr = sorted(list(set([-x for x in nums2])))
        idx = list(range(n))
        idx.sort(key = lambda x: -nums1[x])
        # print(idx)
        ans = [0]*m 
        mt = [-1]*(len(arr)+1)
        cur = 0
        for q in qs:
            while cur < n and nums1[idx[cur]] >= queries[q][0]:
                i = bisect_left(arr,-nums2[idx[cur]])+1
                update(i,nums1[idx[cur]]+nums2[idx[cur]],mt)
                cur += 1 
            i = bisect_right(arr,-queries[q][1])
            # print(q,i,arr)
            ans[q] = query(i,mt)
        return ans 

