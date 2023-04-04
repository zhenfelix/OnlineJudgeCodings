
// 携程校招-2022.9.28-k-好数组
// 题目解析以及代码

// 关注公众号:塔子哥学算法，搜索“P1010”即可得到对应题解
// k-好数组
// 题目大意

// 定义 k-好数组为一个数组中的每个长度为k的连续子数组的和相等。

// 给定一个数组，每次操作可以将数组中的一个数+1，求用 至多xx 次操作将这个数组变为一个 k-好数组 后的最大值为多少，如果不能变成一个 k-好数组 则输出 −1−1
// 输入描述

// 第一行nn，kk，xx，分别表示数组长度，k好数组长度，操作次数

// 第二行nn个数aa，表示数组元素

// 1≤k,n,x≤1000001≤k,n,x≤100000 , k≤k≤n

// −109≤a≤109−109≤a≤109
// 样例

// 输入

// 5 3 10
// 1 2 3 4 5

// 输出

// 7

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
    int n, k, x;
    ll ans = 0;
    cin >> n >> k >> x;
    vector<int> arr(n), mx(k,0), cnt(k,0);
    int j = 0;
    for (int i = 0; i < n; i++){
        cin >> arr[i];
        mx[i%k] = max(mx[i%k], arr[i]);
        cnt[i%k]++;
        if (mx[i%k] > mx[j]) j = i%k;
    }
    for (int i = 0; i < n; i++){
        x -= (mx[i%k]-arr[i]);
    }
    if (x < 0){
        cout << -1 << endl;
        return;
    }
    cout << mx[j] + x / cnt[j] << endl;
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
