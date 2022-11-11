class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2,3,5,7,11,13,17,19,23,29]
        states = list(range(31))
        for i in range(2,31):
            s = 0
            for j, p in enumerate(primes):
                if i%p == 0:
                    if i%(p*p) == 0:
                        s = 0
                        break  
                    s |= (1<<j)
            states[i] = s 
        # print(states)
        n = len(primes)
        MOD = 10**9+7 
        dp = [0]*(1<<n)
        dp[0] = 1
        cc = Counter(nums)
        for v in range(2,31):
            if states[v] == 0 or cc[v] == 0:
                continue
            for s in range(1,1<<n)[::-1]:
                if (s&states[v]) != states[v]:
                    continue
                dp[s] += dp[s^states[v]]*cc[v]
                dp[s] %= MOD 
            # print(v,dp[:10],sum(dp))
        return (pow(2,cc[1],MOD)*sum(dp[1:]))%MOD



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

