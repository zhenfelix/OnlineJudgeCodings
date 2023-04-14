class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def calc(arr):
            r = sum(arr)
            l = 0  
            m = len(arr)
            ans = []
            for i, a in enumerate(arr):
                r -= a 
                ans.append(r-a*(m-1-i)+a*i-l)
                l += a 
                
            return ans 
        mp = defaultdict(list)
        for i, v in enumerate(nums):
            mp[v].append(i)
        res = [0]*n 
        for _, vs in mp.items():
            delta = calc(vs)
            # print(vs,delta)
            for i, d in zip(vs,delta):
                res[i] = d 
        return res 