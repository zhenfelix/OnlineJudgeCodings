
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

int t, n, m, x, y, c, q, _clock, k, l, pre, cur, cnt, last;

char s[maxn];

std::ostream &operator<<(std::ostream &stream,
                         vector<pii> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}


bool solve()
{
    bool flag = true;
    pre = cur = cnt = 0;
    for (int i = 0; s[i] != '\0'; i++){
        if (s[i] == '#'){
            cnt++;cur--;pre=cur;
            last = i;
        }
        else if (s[i] == '(') cur++;
        else cur--;
        if (cur < 0) flag = false;
    }
    if (cur > pre) flag = false;
    pre -= cur;
    for (int i = last+1; s[i] != '\0'; i++){
        if (s[i] == '(') pre++;
        else pre--;
        if (pre < 0) flag = false;
    }
    return flag;
}

int main()
{
    // freopen("input", "r", stdin);
    scanf("%s\n", s);
    if (!solve()) printf("-1\n");
    else {
        for (int i = 1; i <= cnt; i++){
            if (i < cnt) printf("1\n");
            else printf("%d\n", cur+1);
        }
    }

}
