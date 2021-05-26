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
    int n, m, q, k;
    cin >> n >> m;
    vector<vector<bool>> edges(n+1, vector<bool>(n+1, false));
    while (m--)
    {
        int a, b;
        cin >> a >> b;
        edges[a][b] = true;
        edges[b][a] = true;
    }
    cin >> q;
    while (q--)
    {
        cin >> k;
        vector<int> arr(k);
        set<int> seen;
        for (int i = 0; i < k; i++)
            cin >> arr[i];
        bool flag = true;
        if (arr[0] == arr[k-1]){
            for (int i = 1; i < k; i++){
                seen.insert(arr[i]);
                if (!edges[arr[i]][arr[i-1]]){
                    flag = false;
                    break;
                }
            }
            if (seen.size() != n || k-1 != n)
                flag = false;
        }
        else{
            flag = false;
        }
        if (flag)
            cout << "YES\n";
        else
            cout << "NO\n";
    }
    
    return 0;
}
