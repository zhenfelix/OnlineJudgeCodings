# 第五题:题目内容

# 有一个任务jobjob和两个机器m1,m2m1,m2。执行这个任务的消耗为一个正整数cost(1≤cost≤2×105)cost(1≤cost≤2×105)，现在考虑到机器的负荷不能太大，因此我们需要将这个任务切割成k(1≤k≤cost)k(1≤k≤cost)个子任务，将它们分发给两个机器。由于技术所限，必须由第一个机器按切割顺序执行若干个子任务，然后再由第二个机器执行剩下的子任务。我们希望最终两个机器的消耗是相等的。请你编写一个函数，返回合法的切割方案数。由于答案可能过大你需要将答案对109+7109+7取模
# 样例11

# 输入

# 6, 3

# 输出

# 4

# 说明
# 共有4种切割方式:
# 6=1+2+3(前两个分配给1号机器，第三个分配给2号机器)。
# 6=2+1+3 (前两个分配给1号机器，第三个分配给2号机器)。
# 6=3+1+2 (第一个分配给1号机器，后两个分配给2号机器)。
# 6=3+2+1 (第一个分配给1号机器，后

# 作者：塔子哥学算法
# 链接：https://leetcode.cn/circle/discuss/syBnOd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


from random import *
import sys
from collections import * 
from math import * 

def main():
    # sys.stdin = open('contests/input', 'r')
    n, k = list(map(int,input().split()))
    if n%2:
        print(0)
        return
    MOD = 10**9+7
    f = [1]*(n+1)
    for i in range(n):
        f[i+1] = ((i+1)*f[i])%MOD 
    def quickmul(a, q):
        b = 1
        while q:
            if q&1:
                b = (b*a)%MOD 
            a = (a*a)%MOD
            q >>= 1
        return b 
    invf = [1]*(n+1)
    invf[n] = quickmul(f[n],MOD-2)
    for i in range(n)[::-1]:
        invf[i] = ((i+1)*invf[i+1])%MOD
    # for i in range(n):
    #     assert((f[i]*invf[i])%MOD == 1)
    def calc(x,y):
        # if x < y: return 0
        return (f[x]*invf[y]*invf[x-y])%MOD 
    ans = 0
    n //= 2
    # k > n discussion!!!
    for i in range(max(1,k-n),min(k,n+1)):
        ans += calc(n-1,i-1)*calc(n-1,k-i-1)
        ans %= MOD 
    print(ans)

if __name__ == "__main__":
    main()