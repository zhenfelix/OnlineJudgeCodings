class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = []
        for a, b in zip(nums1,nums2):
            arr.append(a-b)
        mi = min(arr)
        # print(arr)
        arr = [a-mi+1 for a in arr]
        mx = max(arr)
        # print(arr)
        tree = [0]*(mx+5)
        def query(pos):
            res = 0
            while pos:
                res += tree[pos]
                pos -= pos&-pos
            return res 
        def update(pos, val):
            while pos <= mx:
                tree[pos] += val
                pos += pos&-pos 
            return
        ans = 0
        for a in arr:
            ans += query(min(max(a+diff,0),mx))
            update(a, 1)
        return ans

