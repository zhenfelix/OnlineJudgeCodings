class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        res = 0
        sums = 0
        presums = [0]
        for i in range(n):
            p, a = fruits[i]
            presums.append(presums[-1]+a)
        # print(presums)
        hi = -1
        for i in range(n):
            if fruits[i][0] < startPos:
                hi = i 
            else:
                break
        hi += 1
        lo = hi-1
        left, right = 0, hi
        while right < n:
            while left < right and fruits[right][0]-startPos+fruits[right][0]-fruits[left][0] > k:
                left += 1
            if fruits[right][0]-startPos+fruits[right][0]-fruits[left][0] > k:
                break
            res = max(res, presums[right+1]-presums[min(hi,left)])
            right += 1
        left, right = lo, n-1
        while left >= 0:
            while left < right and startPos-fruits[left][0]+fruits[right][0]-fruits[left][0] > k:
                right -= 1
            if startPos-fruits[left][0]+fruits[right][0]-fruits[left][0] > k:
                break
            res = max(res, presums[max(lo,right)+1]-presums[left])
            # print(left,right,presums[max(lo,right)+1]-presums[left])
            left -= 1
        return res



class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        
        def helper(p):
            res = 0
            sums = sum(fruits[i][1] for i in range(p))
            left = 0
            # print(fruits, p)
            for right in range(p,n):
                sums += fruits[right][1]
                while left < right and abs(fruits[right][0]-startPos)+abs(fruits[right][0]-fruits[left][0]) > k:
                    if left < p:
                        sums -= fruits[left][1]
                    left += 1
                if abs(fruits[right][0]-startPos)+abs(fruits[right][0]-fruits[left][0]) > k:
                    break
                res = max(res, sums)
            return res 

        ans = 0
        fruits = [(p,a) for p, a in fruits]
        ans = max(ans, helper(bisect.bisect_right(fruits,(startPos,0))))
        fruits = [(-p,a) for p, a in fruits[::-1]]
        startPos = -startPos
        ans = max(ans, helper(bisect.bisect_right(fruits,(startPos,0))))
        return ans 
