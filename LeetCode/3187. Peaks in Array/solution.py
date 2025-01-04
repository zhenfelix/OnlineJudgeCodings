class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        N = n+10
        tree = [0]*N 
        def query(idx):
            v = 0
            while idx:
                v += tree[idx]
                idx -= idx&-idx
            return v  
        def update(idx, v):
            while idx < N:
                tree[idx] += v 
                idx += idx&-idx
            return

        ans = []
        def check(x,y,z):
            return x < y and z < y 
        for i in range(1,n-1):
            if check(nums[i-1],nums[i],nums[i+1]):
                update(i+1,1)

        for t, a, b in queries:
            if t == 1:
                if b-a >= 2:
                    ans.append(query(b)-query(a+1))
                else:
                    ans.append(0)
            else:
                pos, val = a, b 
                if 0 < pos < n-1 and check(nums[pos-1],nums[pos],nums[pos+1]) and not check(nums[pos-1],val,nums[pos+1]):
                    update(pos+1,-1)
                if 0 < pos < n-1 and check(nums[pos-1],val,nums[pos+1]) and not check(nums[pos-1],nums[pos],nums[pos+1]):
                    update(pos+1,1)
                if 0 < pos-1 < n-1 and check(nums[pos-2],nums[pos-1],nums[pos]) and not check(nums[pos-2],nums[pos-1],val):
                    update(pos,-1)
                if 0 < pos-1 < n-1 and check(nums[pos-2],nums[pos-1],val) and not check(nums[pos-2],nums[pos-1],nums[pos]):
                    update(pos,1)
                if 0 < pos+1 < n-1 and check(nums[pos],nums[pos+1],nums[pos+2]) and not check(val,nums[pos+1],nums[pos+2]):
                    update(pos+2,-1)
                if 0 < pos+1 < n-1 and check(val,nums[pos+1],nums[pos+2]) and not check(nums[pos],nums[pos+1],nums[pos+2]):
                    update(pos+2,1)
                nums[pos] = val
        return ans 