# AC but still slow nth_element
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # def nth_element(arr, left, mid, right):
        #     # print(arr,left,mid,right)
        #     if left >= right:
        #         return
        #     lo, hi = left, left
        #     for i in range(left,right+1):
        #         if arr[i] == arr[right]:
        #             arr[i], arr[hi] = arr[hi], arr[i]
        #             hi += 1
        #         elif arr[i] < arr[right]:
        #             tmp = arr[i]
        #             arr[i] = arr[hi]
        #             arr[hi] = arr[lo]
        #             arr[lo] = tmp
        #             hi += 1
        #             lo += 1
        #     if lo <= mid < hi:
        #         return
        #     if mid >= hi:
        #         nth_element(arr, hi, mid, right)
        #     else:
        #         nth_element(arr, left, mid, lo-1)
        #     return

        def nth_element(arr, left, mid, right):
            # print(arr,left,mid,right)
            while left < right:
                lo = hi = left
                for i in range(left,right+1):
                    if arr[i] == arr[right]:
                        arr[i], arr[hi] = arr[hi], arr[i]
                        hi += 1
                    elif arr[i] < arr[right]:
                        tmp = arr[i]
                        arr[i] = arr[hi]
                        arr[hi] = arr[lo]
                        arr[lo] = tmp
                        hi += 1
                        lo += 1
                if lo <= mid < hi:
                    break
                if mid >= hi:
                    left = hi
                else:
                    right = lo-1
            return

        n = len(nums)
        for i in range(n):
            nums[i] = (nums[i] << 18)
        tot = sum(nums)
        half = tot//2
        res = 0 
        lo = 0
        random.shuffle(nums)
        while tot > half:
            mid = (lo+n)//2
            cnt = 0
            nth_element(nums, lo, mid, n-1)
            _tot = tot
            val = nums[mid]
            for i in range(mid,n):
                tmp = nums[i]
                while tmp >= val:
                    tmp //= 2 
                    cnt += 1
                tot -= (nums[i]-tmp)
            # print(lo, mid, n-1, _tot, tot, half)
            if tot >= half:
                res += cnt
                val = nums[mid]
                for i in range(mid,n):
                    while nums[i] >= val:
                        nums[i] //= 2
            else:
                tot = _tot
                if lo == n-1:
                    nums[lo] //= 2
                    tot -= nums[lo]
                    res += 1
                lo = mid
                    
        return res


# TLE nth_element
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        def nth_element(arr, left, mid, right):
            # print(arr,left,mid,right)
            if left >= right:
                return
            pos = left
            for i in range(left,right+1):
                if arr[i] <= arr[right]:
                    arr[i], arr[pos] = arr[pos], arr[i]
                    pos += 1
            if mid+1 == pos:
                return
            if mid+1 < pos:
                nth_element(arr, left, mid, pos-2)
            else:
                nth_element(arr, pos, mid, right)
            return

        n = len(nums)
        for i in range(n):
            nums[i] = (nums[i] << 18)
        tot = sum(nums)
        half = tot//2
        res = 0 
        lo = 0
        
        while tot > half:
            mid = (lo+n)//2
            cnt = 0
            nth_element(nums, lo, mid, n-1)
            _tot = tot
            val = nums[mid]
            for i in range(mid,n):
                tmp = nums[i]
                while tmp >= val:
                    tmp //= 2 
                    cnt += 1
                tot -= (nums[i]-tmp)
            # print(lo, mid, n-1, _tot, tot, half)
            if tot >= half:
                res += cnt
                val = nums[mid]
                for i in range(mid,n):
                    while nums[i] >= val:
                        nums[i] //= 2
            else:
                tot = _tot
                if lo == n-1:
                    nums[lo] //= 2
                    tot -= nums[lo]
                    res += 1
                lo = mid
                    
        return res



class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums)/2
        cur, cnt = 0, 0
        q = [-x for x in nums]
        heapq.heapify(q)
        while cur < target:
            ele = heapq.heappop(q)
            cur -= ele/2
            cnt += 1
            heapq.heappush(q, ele/2)
            # print(cur,cnt)
        return cnt





class Solution:
    def halveArray(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = -(nums[i] << 20)
        heapify(nums)
        ans = 0
        half = sum(nums) >> 1
        while half < 0:
            half -= nums[0] >> 1
            heapreplace(nums, nums[0] >> 1)
            ans += 1
        return ans


# 作者：endlesscheng
# 链接：https://leetcode-cn.com/problems/minimum-operations-to-halve-array-sum/solution/by-endlesscheng-xzk2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。