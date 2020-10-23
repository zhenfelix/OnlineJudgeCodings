import sys
from collections import Counter
# sys.stdin = open("input.txt", "r")


def solve(arr, K):
    nums = sorted(arr)
    n = len(nums)
    lo, hi, tot, res = n, 0, 0, float('inf')
    for i, num in enumerate(nums):
        tot += (K - (num-nums[0]))
    # print(tot)
    nums += [x+K for x in nums]
    # print(nums)
    j = 0
    for i in range(n):
        if i > 0:
            tot += (nums[i]-nums[i-1])*(lo-hi)
        while nums[j] - nums[i] <= K//2:
            hi += 1
            lo -= 1
            tot += (nums[j]-nums[i])
            tot -= (K-(nums[j]-nums[i]))
            # print(i,j,lo,hi,tot,cur)
            j += 1
        hi -= 1
        lo += 1
        res = min(res, tot)
        # print(i, j, lo, hi, cur, tot)

    return res


t = int(input())
for i in range(t):
    W, K = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    res = solve(arr, K)
    print("Case #{}: {}".format(i+1, res))
