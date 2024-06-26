class Solution:
    def maxAbsValExpr(self, arr: List[int], brr: List[int]) -> int:
        dab = [(1,1),(1,-1),(-1,1),(-1,-1)]
        mi = [inf]*4
        ans = 0
        for i, (a,b) in enumerate(zip(arr,brr)):
            tmp = 0
            for j, (fa, fb) in enumerate(dab):
                tmp = max(tmp, fa*a+fb*b+i-mi[j])
                mi[j] = min(mi[j], fa*a+fb*b+i)
            ans = max(ans,tmp)
        return ans



class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        mx1, mx2, mx3, mx4 = -math.inf, -math.inf, -math.inf, -math.inf
        mi1, mi2, mi3, mi4 = math.inf, math.inf, math.inf, math.inf
        for i in range(n):
            mx1 = max(mx1,arr1[i]+arr2[i]+i)
            mi1 = min(mi1,arr1[i]+arr2[i]+i)
            mx2 = max(mx2,arr1[i]+arr2[i]-i)
            mi2 = min(mi2,arr1[i]+arr2[i]-i)
            mx3 = max(mx3,arr1[i]-arr2[i]-i)
            mi3 = min(mi3,arr1[i]-arr2[i]-i)
            mx4 = max(mx4,arr1[i]-arr2[i]+i)
            mi4 = min(mi4,arr1[i]-arr2[i]+i)
        return max(mx1-mi1,mx2-mi2,mx3-mi3,mx4-mi4)
        