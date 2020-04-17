class Solution:
    def sortString(self, s: str) -> str:
        arr = sorted(list(s))
        res = [""]
        while arr:
            # print(arr,res)
            tmp = []
            res.append(arr[0])
            for ch in arr[1:]:
                if ch == res[-1]:
                    tmp.append(ch)
                else:
                    res.append(ch)
            arr = tmp[::-1]
        return ''.join(res)
                    
        