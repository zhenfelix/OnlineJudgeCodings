class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        N = str(n)
        comb = [1]*len(N)
        for i in range(1,len(comb)):
            comb[i] = comb[i-1]*len(digits)

        def dfs(idx):
            if idx == len(N):
                return 1
            cnt = 0
            cnt += sum(x < N[idx] for x in digits)*comb[len(N)-1-idx]
            # cnt += sum(comb[1:len(N)-idx])
            if N[idx] in digits:
                cnt += dfs(idx+1)
            return cnt
        return dfs(0) + sum(comb[1:len(N)])
        