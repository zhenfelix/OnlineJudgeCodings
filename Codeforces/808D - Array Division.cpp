
#include <bits/stdc++.h>
// #include <vector>
// #include <set>
// #include <map>
// #include <algorithm>
// #include <climits>
// #include <iostream>
// #include <unordered_map>
// #include <cstring>
// #include <queue>

#define DEBUG 0

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using tiii = tuple<int,int,int>;
using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 200005+50;
const int maxch = 26;
const int maxm = 2005;

int t, n, m, x, y;
ll MOD = (ll)1e9 + 7, h, w;
int arr[maxn];
unordered_map<ll,int> cnt_left, cnt_right;

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

// void debug_combination(int mx){
//     if (!DEBUG)
//         return;
//     for (int i = 0; i <= mx; i++){
//         for (int j = 0; j <= i; j++){
//             ll val = (((fac[i] * ifac[j]) % MOD) * ifac[i-j]) % MOD;
//             printf("%d %d: %lld; ", i, j, val);
//         }
//     }
// }

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


bool solve()
{
    scanf("%d", &n);
    cnt_left.clear();
    cnt_right.clear();
    ll tot = 0, cur = 0;
    for (int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
        cnt_right[arr[i]]++;
        tot += arr[i];
    }
    if (tot%2 == 1) return false;
    tot >>= 1;
    for (int i = 0; i < n; i++){
        if (arr[i] == tot) return true;
        cur += arr[i];
        cnt_left[arr[i]]++;
        cnt_right[arr[i]]--;
        if (cnt_left[cur-tot] > 0 || cnt_right[tot-cur] > 0) return true;
    }
    return false;
}



int main()
{
#ifndef ONLINE_JUDGE
    freopen("input", "r", stdin);
#endif
    if (solve()) printf("YES\n");
    else printf("NO\n");

}
