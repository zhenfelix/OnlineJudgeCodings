class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        cnt = 0
        for i in range(k):
            st = []
            sz = 0
            for j in range(i,n,k):
                sz += 1
                idx = bisect.bisect_right(st,arr[j])
                if idx >= len(st):
                    st.append(0)
                st[idx] = arr[j]
            cnt += sz-len(st)
        return cnt 