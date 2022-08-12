
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
ll arr[maxn], dist[maxn];

std::ostream &operator<<(std::ostream &stream,
                         vector<pii> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}


ll solve()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; i++) scanf("%lld", &arr[i]);
    sort(arr, arr+m);
    for (int i = 0; i < m; i++){
        dist[i] = i+1 >= m ? arr[0]+n-arr[i]-1 : arr[i+1]-arr[i]-1;
    }
    sort(dist, dist+m);
    ll ans = m, cnt = 0;
    for (int i = m-1; i >= 0; i--){
        ans += min(dist[i], cnt * 2);
        if (dist[i] > cnt*2+1) {ans++; cnt += 2;}
        else if (dist[i] > cnt*2) cnt++;
    }
    return ans;
}



int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    for (int i = 1; i <= t; i++) {
       printf("%lld\n", solve());
    }

}
