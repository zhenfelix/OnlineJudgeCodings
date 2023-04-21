// # 题目内容

// # 曾经有一个小镇叫做“数字王国”，这个小镇以数字相关的工艺和技术而闻名于世。其中最出名的数字工匠就是塔子哥。他被认为是数字领域中最聪明的人之一。他的天赋是发现数字之间的规律，并创造一些有趣的数字游戏。

// # 其中一天，塔子哥想出了一个游戏：删除数字。这个游戏的规则是：给定一个正整数，你需要删除其中连续的一段数字，使得它变成15的倍数。他想知道有多少种不同的删除方式可以达到这个目标。

// # 现在，他把这个问题交给了你。

// # 注：删除的位置不同，即可记为两种不同的方式，并且允许删除后的数存在前导零。同时,不能全删也不能不删
// # 输入描述

// # 输入一个正整数 nn 。 1≤n≤101000001≤n≤10100000
// # 输出描述

// # 一个正整数，代表删除的方案数。
// # 样例

// # 输入

// # 12313565

// # 输出

// # 9


#include <iostream>
#include <string>
#include <vector>
using namespace std;
using ll = long long;
const int MOD = 15;
int main() {
    string s;
    cin >> s;
    int n = s.size();
    vector<int> dp = {0};
    vector<ll> cc(MOD, 0);
    cc[0] += 1;
    for (char ch : s) {
        int a = ch - '0';
        dp.push_back((dp.back() * 10 + a) % MOD);
        cc[dp.back()] += 1;
    }
    ll ans = 0;
    int r2 = 0, base = 1;
    for (int i = n - 1; i >= 0; --i) {
        cc[dp[i + 1]] -= 1;
        for (int r1 = 0; r1 < MOD; ++r1) {
            if ((r1 * base + r2) % MOD == 0) {
                ans += cc[r1];
            }
        }
        r2 = (r2 + base * (s[i] - '0')) % MOD;
        base = (base * 10) % MOD;
    }
    cout << ans - 1 << endl;
    return 0;
}