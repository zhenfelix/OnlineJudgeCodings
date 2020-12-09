class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n, m = len(accounts), len(accounts[0])
        return max(sum(accounts[i]) for i in range(n))