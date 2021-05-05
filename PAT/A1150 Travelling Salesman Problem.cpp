#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;



int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);

    int n, m, a, b, dis, k, t, res = inf, candidate = -1;
    map<pair<int,int>,int> edges;
    
    cin >> n >> m;
    while (m--)
    {
        cin >> a >> b >> dis;
        edges[{a,b}] = dis;
        edges[{b,a}] = dis;
        
        // cout << a << " " << b << endl;
    }
    cin >> k;
    for (int idx = 1; idx <= k; idx++)
    {
        cin >> t;
        vector<int> path(t);
        set<int> visited;
        bool valid = true;
        int cur = 0;
        for (int i = 0; i < t; i++){
            cin >> path[i];
            visited.insert(path[i]);
            if (i > 0){
                if (edges.find({path[i-1],path[i]}) != edges.end()){
                    cur += edges[{path[i - 1], path[i]}];
                }
                else{
                    valid = false;
                }
            }
        }
        bool cycle = (visited.size() == n && path[0] == path[t-1]);
        bool simple_cycle = (cycle && t == n+1);
        if (cycle && valid && cur < res){
            res = cur;
            candidate = idx;
        }
        cout << "Path " << idx << ": ";
        if (valid){
            cout << cur;
        }
        else{
            cout << "NA";
        }
        if (valid && simple_cycle){
            cout << " (TS simple cycle)" << endl;
        }
        else if (valid && cycle){
            cout << " (TS cycle)" << endl;
        }
        else{
            cout << " (Not a TS cycle)" << endl;
        }
    }
    cout << "Shortest Dist(" << candidate << ") = " << res << endl;
}