class Solution:
	def minSideJumps(self, obstacles: List[int]) -> int:
		dp = [1,0,1]
		for x in obstacles[1:]:
			ndp = [float('inf')]*3
			if x > 0:
				dp[x-1] = float('inf')
			for i in range(3):
				if i == x-1:
					continue
				for j in range(3):
					ndp[i] = min(ndp[i], dp[j]+1 if j!=i else dp[j])
			dp = ndp
			# print(dp)
		return min(dp)