
// 2023.3.12-第二题-塔子哥卖玩具
// 题目内容

// 塔子哥是一名玩具店老板，他经营的玩具店以木制小玩具为主要商品。

// 最近，他准备将 NN 个小玩具分装到 MM 个小包装内，并将这些小包装出售。为了使商品价格具有竞争力，他希望限制小包装的总价值不超过 PP，但也不希望价格太低以至于亏本。

// 单个小包装的价值为包装内部玩具数量的平方。

// 因此，他需要找到一种分装方案，使得小包装的总价值恰好为 PP，而且如果存在多种方案，他希望选择字典序最小的那一个。

// 对于两种不同方案 a1,a2,…,aMa1​,a2​,…,aM​ 与 b1,b2,...,bMb1​,b2​,...,bM​若对于 1≤i≤t1≤i≤t 的均有 ai=biai​=bi​,且 at+1<bt+1at+1​<bt+1​ ,那么认为方案 aa 的字典序小于方案 bb 。

// 注意：当 t=0t=0 时，没有合法的ii 存在， 1≤i≤t1≤i≤t 只是限制 ii 的范围。

// 例如，对于 M=3,N=4M=3,N=4 的情况下， 1,1,21,1,2 的字典序小于 2,1,12,1,1 （对应 t=0t=0 的情况）、 1,2,11,2,1 （对应 t=1t=1 的情况）。
// 输入描述

// 第一行三个正整数 N,M,PN,M,P ，含义如题面。 对于所有数据， 1≤M≤N≤121≤M≤N≤12 ， 0≤P≤1090≤P≤109
// 输出描述

// 若不存在任何方案，输出 −1−1 ， 否则输出 MM 个数表示每个小包装内应分的的小玩具数量。
// 样例
// 样例一

// 输入

// 4 3 6

// 输出

// 1 1 2

// 样例二

// 输入

// 4 3 5

// 输出

// -1

// 样例解释

// 不存在方案使得分割后价格和为 55 。

#include<bits/stdc++.h>
using namespace std; 

int main() {
    int n,m,p;
    cin >> n >> m >> p;
    vector<int> path(m,0);
    function<bool(int,int,int)> dfs = [&] (int i, int r, int cost) {
        if (cost > p) return false;
        if (i == m) return (cost == p) && (r == 0);
        if (r <= 0) return false;
        for (int v = 1; v <= r; v++) {
            path[i] = v;
            if (dfs(i+1, r-v, cost+v*v)) return true;
        }
        return false;
    };
    if (!dfs(0,n,0)) {
        cout << -1;
        return 0;
    }
    for (int i = 0; i < m; i++) {
        cout << path[i];
        if (i < m-1) cout << " ";
        else cout << "\n";
    }
    return 0;
}