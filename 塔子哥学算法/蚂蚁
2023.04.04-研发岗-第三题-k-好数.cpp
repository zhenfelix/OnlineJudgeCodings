
// # 2023.04.04-研发岗-第三题-k-好数
// # 题目内容

// # 塔子哥是一名数学爱好者，对数论有浓厚的兴趣。最近，他在研究一种奇特的数字性质，叫做 k−好数k−好数。

// # 他发现，如果一个数可以表示为若干个不同的 kk 的幂之和，那么它就是一个 k−好数k−好数。

// # 例如，1717 就是一个 4−好数4−好数，因为它可以表示为 42+4042+40。但是，88 不是一个 4−好数4−好数，因为它只能表示为 41+4141+41。

// # 塔子哥一直在思考如何判断一个数是否是 k−好数k−好数，并找到了一种有效的方法。

// # 他现在想进一步研究 k−好数k−好数 在区间 [l,r][l,r] 中的分布情况。

// # 他想编写一个程序来解决这个问题，但是他需要一些帮助才能开始。他打算对程序进行 qq 次询问，每次询问一个区间 [l,r][l,r] 中有多少个 k−好数k−好数。
// # 输入描述

// # 第一行输入一个正整数 qq ，代表询问的次数。

// # 接下来的 qq 行，每行输入三个正整数 ll , rr , kk ,代表一次询问。

// # 1≤q≤1031≤q≤103

// # 1≤l,r≤10121≤l,r≤1012

// # 2≤k≤1092≤k≤109
// # 输出描述

// # 输出q行，每行输出一个整数，对应一次询问。
// # 样例

// # 输入

// # 1
// # 15 21 4

// # 输出

// # 4

// # 样例解释

// # 共有 44 个 4−好数4−好数

// # 16=4216=42

// # 17=42+4017=42+40

// # 20=42+4120=42+41

// # 21=42+41+4021=42+41+40


#include <iostream>
#include <cmath>
using namespace std;

long long calc(long long target, long long base) {
    long long lo = 0, hi = 1LL<<41;
    while (lo <= hi) {
        long long m = (lo + hi) / 2;
        long long cur = m;
        long long t = 0;
        long long p = 1;
        while (m) {
            if (m & 1) {
                t += p;
            }
            if (t > target || p > target) {
                t = max(t,p);
                break;
            }
            p *= base;
            m >>= 1;
        }
        if (t <= target) {
            lo = cur + 1;
        } else {
            hi = cur - 1;
        }
    }
    return hi;
}

int main() {
    int q;
    cin >> q;

    for (int i = 0; i < q; i++) {
        long long l, r, k;
        cin >> l >> r >> k;
        cout << calc(r, k) - calc(l - 1, k) << endl;
    }

    return 0;
}