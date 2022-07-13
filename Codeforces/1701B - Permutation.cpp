
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

int t, n, q;
int a[maxn], visited[maxn];
// ll s[maxn], mx;

void solve()
{
    scanf("%d\n", &n);
    printf("%d\n", 2);
    memset(visited, 0, (n+1)*sizeof(int));
    int cnt = 0;
    for (int i = 1; i <= n; i++){
        for (int j = i; j <= n && visited[j] == 0; j *= 2){
            visited[j] = 1;
            cnt += 1;
            printf("%d", j);
            if (cnt < n) printf(" ");
            else printf("\n");
        }
    }
    
}

int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    for(int i = 0; i < t; i++){
        solve();
    }
}
