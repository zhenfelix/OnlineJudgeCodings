class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(mx):
            cnt, sums = 1, 0
            for a in nums:
                # if a > mx:
                #     return False
                if sums+a > mx:
                    cnt += 1
                    sums = 0
                sums += a
                if cnt > m:
                    return False
            return True

        lo, hi = max(nums), sum(nums)
        while lo <= hi:
            mid = (lo+hi)//2
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo



class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lo, hi = max(nums), sum(nums)
        # print(lo,hi)
        
        while lo <= hi:
            cur = cnt = 0
            mid = (lo+hi)//2
            for num in nums:
                cur += num
                if cur > mid:
                    cnt += 1
                    cur = num 
                    if cnt + 1 > m:
                        break
            if cnt + 1 > m:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

