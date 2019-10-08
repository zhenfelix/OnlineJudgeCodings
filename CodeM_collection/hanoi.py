def dfs(n, start, mid, end):
	if n == 1:
		print('move ', n, 'from ', start, 'to ', end)
		return
	dfs(n-1, start, end, mid)
	print('move ', n , 'from ', start, 'to ', end)
	dfs(n-1, mid, start, end)

if __name__ == '__main__':
	dfs(3, 'a', 'b', 'c')