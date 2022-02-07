class Solution:
    def minimumSum(self, num: int) -> int:
        s = str(num)
        res = float('inf')
        for candidate in itertools.permutations(s,4):
            candidate = ''.join(candidate)
            # print(candidate)
            res = min(res, int(candidate[:2])+int(candidate[2:]))
        return res

class Solution:
    def minimumSum(self, num: int) -> int:
        arr = []
        while num:
            arr.append(num%10)
            num //= 10
        arr.sort()
        return (arr[0]+arr[1])*10+arr[2]+arr[3]