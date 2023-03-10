class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cc = Counter(basket1+basket2)
        for k, v in cc.items():
            if v%2:
                return -1
        cc1 = Counter(basket1)
        arr = []
        mx = inf 
        for k in sorted(list(cc.keys())):
            cnt = cc1[k]-cc[k]//2
            mx = min(mx, k)
            for _ in range(abs(cnt)):
                if cnt > 0:
                    arr.append((k,1))
                else:
                    arr.append((k,-1))

        # arr.sort()
        n = len(arr)
        # print(arr,mx,n)
        ans = 0
        for i in range(n//2):
            if arr[i][0] < mx*2:
                ans += arr[i][0]
            else:
                ans += mx*2
        return ans 


