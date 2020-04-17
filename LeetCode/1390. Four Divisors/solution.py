class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def div(x):
            res = [1,x]
            hi = int(math.sqrt(x))
            if hi*hi == x:
                return 0
            for i in range(2,hi+1):
                if x%i == 0:
                    res.append(i)
                    res.append(x//i)
                if len(res) > 4:
                    return 0
            return sum(res) if len(res) == 4 else 0
        
        tmp = list(map(div,nums))
        print(tmp)
        return sum(tmp)
        # return sum(list(map(div,nums)))
                