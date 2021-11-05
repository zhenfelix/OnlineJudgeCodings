class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        cnt = [0]*n 
        pre = 0
        arr = []
        for i, ch in enumerate(s):
            cnt[i] = pre 
            if ch == "*":
                cnt[i] += 1
            else:
                arr.append(i)
            pre = cnt[i]
        res = []
        # print(cnt,arr)
        for left, right in queries:
            l = bisect.bisect_left(arr, left)
            r = bisect.bisect_right(arr, right)-1
            # print(left,right,l,r)
            res.append(0)
            if l < r:
                res[-1] = cnt[arr[r]]-cnt[arr[l]]
        return res





class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        cnt = [0]*n 
        pre = 0
        for i, ch in enumerate(s):
            cnt[i] = pre 
            if ch == "*":
                cnt[i] += 1
            pre = cnt[i]
        left = [n]*n 
        right = [-1]*n 
        for i in range(n):
            if i:
                left[i] = left[i-1]
            if s[i] == "|":
                left[i] = i
        for i in range(n)[::-1]:
            if i < n-1:
                right[i] = right[i+1]
            if s[i] == "|":
                right[i] = i 
        res = []
        # print(cnt)
        # print(left,right)
        for l, r in queries:
            res.append(0)
            if l < r:
                res[-1] = max(0,cnt[left[r]]-cnt[right[l]])
        return res


