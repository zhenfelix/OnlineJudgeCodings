# - [数位 DP 通用模板，附题单（Python/Java/C++/Go）](https://leetcode.cn/problems/count-special-integers/solutions/1746956/shu-wei-dp-mo-ban-by-endlesscheng-xtgx/)



from random import *
import sys
from collections import * 
from math import * 
from functools import *



def solve(a,b):
    def dfs(t, base, pos, r, cnt):
        if t == 0:
            return 0
        cur = t%10
        pre = dfs(t//10, base*10, pos+1, r+cur*base, cnt)
        for i in range(cur):
            if pre == 0 and i == 0: continue
            cnt[i] += base 
        for i in range(10):
            if pre == 0 and i == 0:
                k = 1
                while k < base:
                    cnt[i] -= k 
                    k *= 10
            cnt[i] += cur*(base//10)*(pos-1)
        cnt[cur] += r+1
        return cur+pre*10
    
    cnta = [0]*10
    cntb = [0]*10
    dfs(b,1,1,0,cntb)
    dfs(a-1,1,1,0,cnta)
    for i in range(10): cntb[i] -= cnta[i]
    # print(*cntb)
    return cntb

def solve_another(a,b):
    def countDigitOne(n: int) -> int:
        s = str(n)
        @lru_cache(None)
        def f(i: int, cnt1: int, is_limit: bool, digit: int, zero: bool) -> int:
            if i == len(s):
                return cnt1
            res = 0
            up = int(s[i]) if is_limit else 9
            for d in range(up + 1):  # 枚举要填入的数字 d
                delta = (d == digit)
                if d == digit == 0 and zero: delta = 0
                res += f(i + 1, cnt1 + delta, is_limit and d == up, digit, zero and (d == 0))
            return res
        return [f(0,0,True,i,True) for i in range(10)]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/number-of-digit-one/solutions/1750339/by-endlesscheng-h9ua/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    cntb = countDigitOne(b)
    cnta = countDigitOne(a-1)
    for i in range(10): cntb[i] -= cnta[i]
    # print(*cntb)
    return cntb

def main():
    # sys.stdin = open('contests/input', 'r')
    a, b = list(map(int,input().split()))
    print(*solve_another(a,b))

    # for i in range(1000):
    #     b = randint(1,10000000)
    #     a = randint(1,b)
    #     assert(solve(a,b) == solve_another(a,b))
    #     print(i,a,b,'ok')

if __name__ == "__main__":
    main()