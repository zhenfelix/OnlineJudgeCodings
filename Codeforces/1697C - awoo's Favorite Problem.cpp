
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
using pci = pair<char, int>;

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

std::ostream &operator<<(std::ostream &stream,
                         vector<pci> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}

vector<pci> transform(string &s){
    int n = s.length();
    vector<pci> v;
    for (int i = 0; i < n; i++){
        if (s[i] != 'b') v.push_back({s[i],i});
    }
    return v;
}

bool solve()
{
    scanf("%d\n", &n);
    string s1, s2;
    cin >> s1;
    cin >> s2;
    auto v1 = transform(s1);
    auto v2 = transform(s2);
    // cout << v1 << endl;
    // cout << v2 << endl;
    if (v1.size() != v2.size()) return false;
    int m = v1.size();
    for (int i = 0; i < m; i++){
        auto [ch1, j] = v1[i];
        auto [ch2, k] = v2[i];
        if (ch1 != ch2) return false;
        if (ch1 == 'c'){
            if (j < k) return false;
        }
        else{
            if (j > k) return false;
        }
    }
    
    return true;
    
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
