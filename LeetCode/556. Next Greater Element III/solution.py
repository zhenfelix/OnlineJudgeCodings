class Solution:
    def nextGreaterElement(self, n: int) -> int:
        cur = n
        arr = [cur%10]
        cur //= 10
        while cur:
            tmp = cur%10
            if arr[-1] > tmp:
                idx = 0
                while arr[idx] <= cur%10:
                    idx += 1
                arr[idx], tmp = tmp, arr[idx]
                cur = cur - arr[idx] + tmp
                res, base = 0, 1
                for a in arr:
                    base *= 10
                    res *= 10
                    res += a
                res = cur*base + res
                if res > (1<<31)-1:
                    return -1
                return res
            else:
                arr.append(tmp)
                cur //= 10
            
        return -1
