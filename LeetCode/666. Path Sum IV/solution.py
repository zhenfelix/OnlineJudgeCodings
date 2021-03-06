from collections import *

class Solution:
    def pathSum(self, nums: List[int]) -> int: 
        if not nums:
            return 0
        n = len(nums)
        left, right = [-1]*n, [-1]*n 
        mp = {}
        for i, val in enumerate(nums):
            depth, pos = val//100, val//10%10
            mp[depth,pos] = i 
        self.res = 0
        # print(mp)
        def dfs(cur,sums):
            val = nums[cur]
            sums += val%10
            depth, pos = val//100, val//10%10
            if (depth+1,pos*2-1) not in mp and (depth+1,pos*2) not in mp:
                self.res += sums
            if (depth+1,pos*2-1) in mp:
                dfs(mp[depth+1,pos*2-1],sums)
            if (depth+1,pos*2) in mp:
                dfs(mp[depth+1,pos*2],sums)
            return
        dfs(0,0)
        return self.res 


        

