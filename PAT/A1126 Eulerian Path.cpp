#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;


int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
//     freopen("input", "r", stdin);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> graph(n+1);

    while (m--)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    int odds = 0;
    queue<int> q;
    vector<int> visited(n+1,false);
    q.push(1);
    visited[1] = true;
    int cnt = 0;
    while (!q.empty()){
        int cur = q.front(); q.pop();
        cnt++;
        for (auto nxt : graph[cur]){
            if (!visited[nxt]){
                visited[nxt] = true;
                q.push(nxt);
            }
        }
    }
    // bool isolation = false;
    for (int i = 1; i <= n; i++){
        if (i > 1)
            cout << " ";
        int len = graph[i].size();
        // if (len)
            cout << len;
        if (len&1)
            odds++;
        // if (len == 0)
        //     isolation = true;
    }
    cout << "\n";
    if (cnt != n || odds == 1 || odds > 2)
        cout << "Non-Eulerian";
    else if (odds == 2)
        cout << "Semi-Eulerian";
    else
        cout << "Eulerian";


    return 0;
}
