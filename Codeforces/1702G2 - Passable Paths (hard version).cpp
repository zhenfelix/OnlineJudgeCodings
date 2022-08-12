
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
const int maxn = 200005;
const int maxch = 26;
const int maxm = 20;

int t, n, m, x, y, c, q, _clock;
vector<vector<int>> g(maxn);
int tin[maxn], tout[maxn], arr_tin[maxn], arr_tout[maxn], marked[maxn];
int ancestor[maxn][maxm];

std::ostream &operator<<(std::ostream &stream,
                         vector<pii> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}

void dfs(int cur, int parent){
    _clock++;
    tin[cur] = _clock;
    if (cur == parent){
        for (int i = 0; i < maxm; i++) ancestor[cur][i] = cur;
    }
    else{
        ancestor[cur][0] = parent;
        for (int i = 1; i < maxm; i++) ancestor[cur][i] = ancestor[ancestor[cur][i-1]][i-1];
    }
    for (auto nxt : g[cur]){
        if (nxt == parent) continue;
        dfs(nxt, cur);
    }
    _clock++;
    tout[cur] = _clock;
}

bool isAncestor(int u, int v){
    return tin[u] < tin[v] && tout[u] > tout[v];
}

int lca(int u, int v){
    if (isAncestor(u,v)) return u;
    if (isAncestor(v,u)) return v;
    for (int i = maxm-1; i >= 0; i--){
        if (!isAncestor(ancestor[u][i],v)) u = ancestor[u][i];
    }
    return ancestor[u][0];
}

tiii check(){
    int cnt = 0, head = 0, tail = 0, right = m-1;
    for (int left = 0; left < m; left++){
        if (marked[arr_tin[left]])
            continue;
        while (right >= 0 && left < m && (marked[arr_tout[right]] || arr_tin[left] != arr_tout[right]))
            right--;
        if (right >= 0 && left < m && arr_tin[left] == arr_tout[right]){
            cnt++;
            marked[arr_tin[left]] = true;
            if (head == 0) head = arr_tin[left];
            tail = arr_tin[left];
        }
    }
    return {cnt,head,tail};
}

void debug()
{
    for (int i = 0; i < n; i++)
        cout << i + 1 << " tin: " << tin[i + 1] << " tout: " << tout[i + 1] << "; ";
    cout << endl;
}

void debug2(){
    for (int i = 0; i < m; i++)
        cout << arr_tin[i] << " ";
    cout << endl;
    for (int i = 0; i < m; i++)
        cout << arr_tout[i] << " ";
    cout << endl;
}

bool solve()
{
    scanf("%d\n", &m);
    for (int i = 0; i < m; i++){
        scanf("%d", &x);
        arr_tin[i] = x;
        arr_tout[i] = x;
        marked[x] = false;
    }
    if (m <= 2) return true;
    sort(arr_tin, arr_tin+m, [](int a, int b){return tin[a] < tin[b];});
    sort(arr_tout, arr_tout+m, [](int a, int b){return tout[a] < tout[b];});
    // debug2();
    auto [cnt1, head1, tail1] = check();
    auto [cnt2, head2, tail2] = check();
    // cout << cnt1 << " " << head1 << "; " << cnt2 << " " << head2 << endl;
    if (cnt1+cnt2 < m) return false;
    if (head1 > 0 && head2 > 0 && isAncestor(head1, head2) && lca(tail1,tail2) != head1) return false;
    return true;
}

int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &n);
    for (int i = 1; i < n; i++){
        scanf("%d%d", &x, &y);
        g[x].push_back(y);
        g[y].push_back(x);
    }
    _clock = 0;
    dfs(1,1);
    // debug();
    scanf("%d", &q);
    for(int i = 0; i < q; i++){
        if (solve()){
            printf("YES\n");
        }
        else{
            printf("NO\n");
        }
    }

}
