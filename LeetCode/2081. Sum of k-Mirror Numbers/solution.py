class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def convert(x):
            nums = []
            while x:
                nums.append(x%k)
                x //= k 
            left, right = 0, len(nums)-1
            while left <= right:
                if nums[left] != nums[right]:
                    return False
                left += 1
                right -= 1
            # print(nums)
            return True
        
        res = 0
        cnt = 0

        for sz in range(1,15):
            def dfs(i, val, arr):
                nonlocal res
                nonlocal cnt
                if cnt >= n:
                    return
                if i == sz:
                    if convert(val):
                        res += val
                        cnt += 1
                    return
                if i >= (sz+1)//2:
                    t = arr[sz-1-i]
                    dfs(i+1, val*10+t, arr+[t])
                else:
                    mi = 0 if i else 1
                    for t in range(mi,10):
                        dfs(i+1, val*10+t, arr+[t])
                return
            dfs(0, 0, [])
            if cnt >= n:
                return res
        return res 