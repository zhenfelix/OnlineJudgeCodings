
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
char a[maxn], b[maxn];

std::ostream &operator<<(std::ostream &stream,
                         vector<pii> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}


bool solve()
{
    scanf("%d%d", &n, &m);
    scanf("%s", a);
    scanf("%s", b);
    bool flag = true;
    int i = n-1, j = m-1;
    while (j > 0) if(a[i--] != b[j--]) {flag = false; break;}
    if (flag) {
        while (i >= 0) {
            if (a[i] == b[j])
                break;
            i--;
        }
    }
    if (i < 0) flag = false;
    return flag;
}



int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    for (int i = 1; i <= t; i++) {
       if (solve()) printf("YES\n");
       else printf("NO\n");
    }

}
