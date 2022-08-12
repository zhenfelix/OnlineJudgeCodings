
// #include <bits/stdc++.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>
#include <cstring>
#include <queue>

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using tiii = tuple<int,int,int>;
using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 200005+50;
const int maxch = 26;
const int maxm = 20;

int t, n, m, x, y, c, q, _clock, k, pre, cur, last;
int arr[maxn];

std::ostream &operator<<(std::ostream &stream,
                         vector<pii> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}


int solve()
{
    scanf("%d%d", &n, &x);
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int cnt = 0, mi = arr[0], mx = arr[0];
    for (int i = 1; i < n; i++){
        mi = min(mi, arr[i]);
        mx = max(mx, arr[i]);
        if (mx-mi > x*2){
            cnt++;
            mi = mx = arr[i];
        }
    }
    return cnt;
}



int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    for (int i = 1; i <= t; i++) {
       printf("%d\n", solve());
    }

}
