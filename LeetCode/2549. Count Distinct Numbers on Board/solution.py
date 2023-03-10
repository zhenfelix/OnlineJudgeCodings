class Solution:
    def distinctIntegers(self, n: int) -> int:
        arr = [n] 
        
        while True:
            # print(arr)
            narr = set(arr)
            for i in range(1,n+1):
                for a in arr:
                    if a%i == 1:
                        narr.add(i)
                        break 
                    
            narr = list(narr)
            if len(arr) == len(narr):
                break
            arr = narr
        return len(arr)