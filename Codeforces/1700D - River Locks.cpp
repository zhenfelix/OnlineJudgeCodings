
// #include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>
#include <cstring>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 200005;

int n, q;
int a[maxn];
ll s[maxn], mx[maxn];

// void solve()
// {
//     int t;
//     scanf("%d\n", &t);
//     int ans = 0;
//     for (int i = 1; i <= n; i++){
//         int cnt = (s[i]-1)/t+1;
//         if (cnt > i){
//             ans = -1;
//             break;
//         }
//         ans = max(ans, cnt);
//     }
//     printf("%d\n", ans); 
// }

void solve()
{
    int t;
    scanf("%d\n", &t);
    if (t < mx[n]){
        printf("-1\n");
        return;
    }
    int lo = 1, hi = n;
    while (lo <= hi){
        int mid = (lo+hi)/2;
        // if (t >= mx[mid] && (ll)t*mid >= s[n]){
        //     hi = mid - 1;
        // }
        if ((ll)t * mid >= s[n])
        {
            hi = mid - 1;
        }
        else{
            lo = mid + 1;
        }
    }
    // if (lo > n) lo = -1;
    printf("%d\n", lo);
}

int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    s[0] = 0;
    mx[0] = 0;
    for (int i = 1; i <= n; i++) {
        s[i] = s[i - 1] + (ll)a[i - 1];
        mx[i] = max(mx[i-1], (s[i]-1)/i+1);
    }
    scanf("%d\n", &q);
    for(int i = 0; i < q; i++){
        solve();
    }
}








// #include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>
#include <cstring>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 200005;

int n, q;
int a[maxn];
ll s[maxn], mx;

// void solve()
// {
//     int t;
//     scanf("%d\n", &t);
//     int ans = 0;
//     for (int i = 1; i <= n; i++){
//         int cnt = (s[i]-1)/t+1;
//         if (cnt > i){
//             ans = -1;
//             break;
//         }
//         ans = max(ans, cnt);
//     }
//     printf("%d\n", ans); 
// }

void solve()
{
    int t, ans = -1;
    scanf("%d\n", &t);
    if (t >= mx){
        ans = (s[n] - 1) / t + 1;
    }
    printf("%d\n", ans);
}

int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    s[0] = 0;
    mx = 0;
    for (int i = 1; i <= n; i++) {
        s[i] = s[i - 1] + (ll)a[i - 1];
        mx = max(mx, (s[i]-1)/i+1);
    }
    scanf("%d\n", &q);
    for(int i = 0; i < q; i++){
        solve();
    }
}
