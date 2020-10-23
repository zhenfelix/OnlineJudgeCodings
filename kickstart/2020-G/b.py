import sys
# sys.stdin = open("input.txt", "r")


def solve(mat):
    n = len(mat)
    dp = [0]*(2*n)
    for i in range(n):
        for j in range(n):
            dp[i-j] += mat[i][j]
    return max(dp)


t = int(input())
for i in range(t):
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append(list(map(int,input().split())))
    # print(mat)
    res = solve(mat)
    print("Case #{}: {}".format(i+1,res))

