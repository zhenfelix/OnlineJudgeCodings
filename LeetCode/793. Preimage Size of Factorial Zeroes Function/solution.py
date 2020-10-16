class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        def count(x, b):
            base, cnt = b, 0
            while x//base:
                cnt += x//base
                base *= b 
            return cnt

        def f(x):
            return min(count(x,2),count(x,5))

        def search(target):
            lo, hi = 0, 10**10
            while lo <= hi:
                mid = (lo+hi)//2
                if f(mid) <= target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo
        
        print(f(10**10))
    
        return search(K)-search(K-1)
        # return 0