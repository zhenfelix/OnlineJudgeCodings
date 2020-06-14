class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        res = []
        arr.sort()
        i, j = 0, len(arr)-1
        m = j//2
        while k:
            if abs(arr[i]-arr[m]) > abs(arr[j]-arr[m]):
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j -= 1
            k -= 1
        return res
            
        