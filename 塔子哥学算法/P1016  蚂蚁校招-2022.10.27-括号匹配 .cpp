
// 蚂蚁校招-2022.10.27-括号匹配
// 题目解析以及代码

// 关注公众号:塔子哥学算法，搜索“P1016”即可得到对应题解
// 括号匹配
// 题目内容

// 给定个仅包含 ( 、 ) 和 ? 三种字符构成的字符串，? 字符可以代替左括号或者右括号。

// 请问该字符串可以代表多少种不同的合法括号序列?
// 输入描述

// 一个仅包含( 、) 和 ? 的字符串，长度不超过 20002000 。
// 输出描述

// 合法序列的数量。由于数量可能过大，请对 109+7109+7 取模。
// 样例

// 输入

// ????(?

// 输出

// 2

// 样例解释

// 共有 22 种不同的合法括号序列， () () () 或 (()) ()



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
    int n;
    const int MOD = 1e9+7;
    string s;
    cin >> s;
    n = s.length();
    vector<ll> dp(n+1,0);
    dp[0] = 1;
    for (auto &ch : s){
        vector<ll> ndp(n+1,0);
        for (int i = 0; i <= n; i++){
            if (i > 0 && (ch == '(' || ch == '?')) ndp[i] = (ndp[i]+dp[i-1])%MOD;
            if (i < n && (ch == ')' || ch == '?')) ndp[i] = (ndp[i]+dp[i+1])%MOD;
        }
        swap(dp,ndp);
    }
    cout << dp[0] << endl;
    
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
