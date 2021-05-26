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
    int k, n;
    cin >> k;
    while (k--)
    {
        int x;
        bool flag = true;
        set<int> row, diag, antidiag;
        cin >> n;
        for (int i = 1; i <= n; i++){
            cin >> x;
            if (row.find(x) != row.end() || diag.find(x-i) != diag.end() || antidiag.find(x+i) != antidiag.end()){
                flag = false;
                // break;
            }
            row.insert(x);
            diag.insert(x-i);
            antidiag.insert(x+i);
        }
        if (flag)
            cout << "YES\n";
        else 
            cout << "NO\n";
    }

    return 0;
}
