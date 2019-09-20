class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        if n == 1:
            return ["0","1","8"]
        if n == 2:
            return ["11","69","88","96"]
        
        dp = {}
        dp[0] = self.findStrobogrammatic(0)
        dp[1] = self.findStrobogrammatic(1)
        dp[2] = self.findStrobogrammatic(2)
        for i in range(3,n+1):
            dp[i] = [ch[0]+('0'*j)+mid+('0'*j)+ch[-1] for j in range(0,(i-2)//2+1) for mid in dp[i-2-2*j] for ch in dp[2]]
            
        # print(len(dp[n]))
        return dp[n]