
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

const int inf = 0x3f3f3f3f;
const int maxn = 200005;
const int maxch = 26;

int t, n, m, x, y;
// int a[maxn], b[maxn], idx[maxn], lo[maxn], hi[maxn];
// ll u[maxn];
ll p;
string s;
ll cnt[maxch];
// ll s[maxn], mx;


bool solve()
{
    scanf("%d\n", &n);
    unordered_map<int,int> cc;
    bool flag = true;
    // vector<int> arr;
    // vector<pii> arr;
    // bool flag = true;
    for (int i = 0; i < n; i++){
        scanf("%d", &x);
        while (x%2 == 0) x /= 2;
        cc[x]++;
    }
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &x);
        if (flag){
            while (x % 2 == 0)
                x /= 2;
            while (x && (cc.find(x) == cc.end() || cc[x] == 0))
                x /= 2;
            if (x == 0)
                flag = false;
            cc[x]--;
        }
    }
    
    return flag;
    
}

int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    for(int i = 0; i < t; i++){
        if (solve()){
            printf("YES\n");
        }
        else{
            printf("NO\n");
        }
    }
}
