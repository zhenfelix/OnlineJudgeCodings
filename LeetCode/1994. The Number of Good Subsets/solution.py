class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        MOD = 10**9+7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mp = {6:3, 10:5, 14:9, 15:6, 21:10, 22:17, 26:33, 30:7}
        for i in range(10):
            mp[primes[i]] = (1<<i)
        cc = Counter(nums)
        # print(cc)
        res = [0]
        arr = [(k,v) for k, v in mp.items()]
        # print(arr)
        n = len(arr)
        # def dfs(i, cur, sums, path):
            # if i == n:
                # if cur:
                    # print(path,cur,sums)
                    # res[0] += sums
                    # res[0] %= MOD
                # return
            # 
            # k = arr[i][0]
            # v = arr[i][1]
            # cnt = cc[k]
            # if cnt and cur&v == 0:
                # dfs(i+1, cur|v, sums*cnt%MOD, path+[k])
            # dfs(i+1, cur, sums, path)

        # dfs(0,0,1,[])


        def dfs(i, cur, sums):
            if i == n:
                if cur:
                    # print(path,cur,sums)
                    res[0] += sums
                    res[0] %= MOD
                return
            
            k = arr[i][0]
            v = arr[i][1]
            cnt = cc[k]
            if cnt and cur&v == 0:
                dfs(i+1, cur|v, sums*cnt%MOD)
            dfs(i+1, cur, sums)
        dfs(0,0,1)
        
        return (pow(2,cc[1],MOD)*res[0])%MOD

