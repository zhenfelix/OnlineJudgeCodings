
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
using tiii = tuple<int,int,int>;
using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 200005+50;
const int maxch = 26;
const int maxm = 110;

int t, n, m, x, y, c, p, q, k, last, cur, s;
ll MOD = 998244353;

vector<vector<int>> lines(4);

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


bool solve()
{
    ll d1, d2, d3, d12, d23, d13, tot;
    scanf("%d%lld%lld%lld", &n, &d12, &d23, &d13);
    tot = d12+d23+d13;
    if (tot%2 == 1) return false;
    tot /= 2;
    d1 = tot-d23, d2 = tot-d13, d3 = tot-d12;
    tot = 0;
    int cnt = 0;
    vector<ll> tmp {0, d1, d2, d3 };
    int center = 4;
    for (int i = 1; i <= 3; i++){
        if (tmp[i] < 0) return false;
        if (tmp[i] == 0){
            cnt++;
            center = i;
        }
        tot += tmp[i];
    }
    
    if (cnt > 1) return false;
    tot++;
    if (tot > n) return false;
    cur = center == 4 ? 5 : 4;
    
    for (int i = 1; i <= 3; i++){
        lines[i].clear();
        lines[i].push_back(i);
        if (tmp[i] > 0){
            for (int j = 1; j < tmp[i]; j++){
                lines[i].push_back(cur++);
            }
            lines[i].push_back(center);
        }
    }
    while (cur <= n){
        lines[1].push_back(cur++);
    }
    return true;  
}



int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    for (int i = 1; i <= t; i++) {
        if (solve()){
            printf("YES\n");
            for (int j = 1; j <= 3; j++){
                m = lines[j].size();
                for (int k = 1; k < m; k++){
                    printf("%d %d\n", lines[j][k-1], lines[j][k]);
                }
            }
        }
        else{
            printf("NO\n");
        }
    }

}
