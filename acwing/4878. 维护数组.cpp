# 给定一个长度为 n 的整数序列 d1,d2,…,dn 以及三个整数 k,a,b

# 。

# 初始时，所有 di
# 均为 0

# 。

# 你需要对序列依次进行 q

# 次操作，操作分为以下两种：

#     1 x y，将 dx

# 增加 y
# 。
# 2 p，计算并输出 ∑i=1p−1min(di,b)+∑i=p+knmin(di,a)

#     。

# 输入格式

# 第一行包含 5
# 个整数 n,k,a,b,q

# 。

# 接下来 q

# 行，每行描述一个操作，格式如题面所述。
# 输出格式

# 每个 2 p 操作，输出一行一个整数表示结果。
# 数据范围

# 前 3
# 个测试点满足 1≤k≤n≤10，1≤q≤10。
# 所有测试点满足 1≤k≤n≤2×105，1≤b<a≤10000，1≤q≤2×105，1≤x≤n，1≤y≤10000，1≤p≤n−k+1

# 。
# 输入样例1：

# 5 2 2 1 8
# 1 1 2
# 1 5 3
# 1 2 1
# 2 2
# 1 4 2
# 1 3 2
# 2 1
# 2 3

# 输出样例1：

# 3
# 6
# 4

# 输入样例2：

# 5 4 10 1 6
# 1 1 5
# 1 5 5
# 1 3 2
# 1 5 2
# 2 1
# 2 2

# 输出样例2：

# 7
# 1

# 难度： 困难
# 时/空限制： 1s / 256MB
# 总通过数： 284
# 总尝试数： 896
# 来源： AcWing,第96场周赛
# 算法标签
from random import *
import sys
from collections import * 
from math import * 
from functools import *



#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
int n, k, a, b, q;
int treea[N], treeb[N], arr[N];

void update(int tree[], int i, int v, int nmax)
{
    while (i <= nmax)
    {
        tree[i] += v;
        i += (i & -i);
    }
}

int query(int tree[], int i)
{
    int res = 0;
    while (i)
    {
        res += tree[i];
        i -= (i & -i);
    }
    return res;
}

void solve()
{
    cin >> n >> k >> a >> b >> q;
    int nmax = n+10;
    for (int i = 1; i <= n; i++)
    {
        treea[i] = 0;
        treeb[i] = 0;
        arr[i] = 0;
    }
    for (int i = 0; i < q; i++)
    {
        int op;
        cin >> op;
        if (op == 1){
            int x, y;
            cin >> x >> y;
            update(treea, x, min(y, max(0, a - arr[x])), nmax);
            update(treeb, x, min(y, max(0, b - arr[x])), nmax);
            arr[x] += y;
        }
        else
        {
            int p;
            cin >> p;
            int l = query(treeb, p - 1);
            int r = 0;
            if (p + k <= n)
            {
                r = query(treea, n) - query(treea, p + k - 1);
            }
            cout << l + r << endl;
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // freopen("contests/input", "r", stdin);
    // string s;
    // int case;
    for (int i = 1; i <= 1; i++)
    {
        // cin >> n >> m >> v >> w;
        solve();
        // cout << solve(n, m, vs, ws, cnts) << endl;
        // if (solve(n, l, r)) {
        //     cout << "Yes" << endl;
        // } else {
        //     cout << "No" << endl;
        // }
    }
    // int a, b;
    // for (int i = 0; i < 1000; i++) {
    //     b = rand() % 10000000 + 1;
    //     a = rand() % b + 1;
    //     assert(solve(a, b) == solve_another(a, b));
    //     cout << i << " " << a << " " << b << " ok" << endl;
    // }
    return 0;
}
