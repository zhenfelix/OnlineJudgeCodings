
// 米哈游春招后端-2023.03.19-第一题-米哈游的RBG矩阵
// 题目解析以及代码

// 关注公众号:塔子哥学算法，搜索“P1094”即可得到对应题解
// 题目内容

// 米小游拿到了一个矩阵，矩阵上有一格有一个颜色，为红色( R )。绿色( G )和蓝色( B )这三种颜色的一种。

// 然而米小游是蓝绿色盲，她无法分游蓝色和绿色，所以在米小游眼里看来，这个矩阵只有两种颜色，因为蓝色和绿色在她眼里是一种颜色。

// 米小游会把相同颜色的部分看成是一个连通块。请注意，这里的连通划是上下左右四连通的。

// 由于色盲的原因，米小游自己看到的连通块数量可能比真实的连通块数量少。

// 你可以帮米小游计算连通块少了多少吗？
// 输入描述

// 第一行输入两个正整数 nn 和 mm ，代表矩阵的行数和列数。

// 接下来的 nn 行，每行输入一个长度为 mm 的，仅包含 R 、G 、B 三种颜色的字符串，代表米小游拿到的矩阵。

// 1≤n,m≤10001≤n,m≤1000
// 输出描述

// 一个整数，代表米小游视角里比真实情况少的连通块数量。
// 样例

// 输入

// 2 6
// RRGGBB
// RGBGRR

// 输出

// 3

// 样例解释

// 米小游视角里有 33 个连通块，而实际上有 66 个连通块，所以米小游视角的连通块数量比真实情况少了 33 个。


#include <bits/stdc++.h>
using namespace std;

#define DEBUG 0

using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using tiii = tuple<int,int,int>;
using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const ll MOD = 1e9+7;

std::ostream &operator<<(std::ostream &stream,
                         vector<pii> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}

std::ostream &operator<<(std::ostream &stream,
                         vector<int> &v)
{
    for (auto x : v)
        stream << x << "-";
    return stream;
}

std::ostream &operator<<(std::ostream &stream,
                         vector<ll> &v)
{
    for (auto x : v)
        stream << x << "-";
    return stream;
}

template<class T>
void debug_arr(T a[], int start, int end){
    if (!DEBUG) return;
    for (int i = start; i <= end; i++) cout << a[i] << " ";
    cout << endl;
}

bool myless(string a, string b){
    return a.length() < b.length() || (a.length() == b.length() && a < b);
}

ll quickmulti(ll a, ll p){
    ll ans = 1;
    while (p){
        if (p&1) ans = (ans*a)%MOD;
        a = (a*a)%MOD;
        p >>= 1;
    }
    return ans;
}


void solve()
{
    int n, m;
    cin >> n >> m;
    vector<vector<char>> mat(n, vector<char>(m));
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) cin >> mat[i][j];
    vector<int> parent(n*m);
    
    function<int(int)> find = [&](int x) -> int {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    };
    function<void(int,int)> connect = [&] (int x, int y) {
        auto rx = find(x);
        auto ry = find(y);
        if (rx != ry) parent[rx] = ry;
        return;
    };
    function<int(bool)> calc = [&](bool flag) -> int
    {
        for (int i = 0; i < n * m; i++)
            parent[i] = i;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (i){
                    if (mat[i-1][j] == mat[i][j] || (flag && mat[i-1][j] != 'R' && mat[i][j] != 'R'))
                    connect((i-1)*m+j, i*m+j);
                }
                if (j){
                    if (mat[i][j-1] == mat[i][j] || (flag && mat[i][j-1] != 'R' && mat[i][j] != 'R'))
                    connect((i*m+j-1),i*m+j);
                }
            }
        }
        vector<int> p(n*m);
        for (int i= 0; i < n*m; i++) p[i] = find(i);
        unordered_set<int> s(p.begin(), p.end());
        return s.size();
    };
    auto s1 = calc(true);
    auto s2 = calc(false);
    cout << s2-s1 << endl;
    return;
}



int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// #ifndef ONLINE_JUDGE
//     freopen("contests/input", "r", stdin);
// #endif
    solve();

}
