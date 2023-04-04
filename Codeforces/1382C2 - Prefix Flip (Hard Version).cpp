#include<bits/stdc++.h>
using namespace std;

int main()
{
    // freopen("contests/input","r",stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t, n;
    string sa, sb;
    cin >> t;
    while (t--)
    {
        cin >> n;
        cin >> sa;
        cin >> sb;
        vector<int> ans;
        char ch = sa[0];
        for (int i = 0; i < n-1; i++){
            if (ch != sa[i+1]){
                ch = sa[i+1];
                ans.push_back(i+1);
            }
        }
        for (int i = n-1; i >= 0; i--){
            if (ch != sb[i]){
                ch = sb[i];
                ans.push_back(i+1);
            }
        }
        cout << ans.size();
        for (auto &p : ans){
            cout << " " << p;
        }
        cout << endl;
    }
    return 0;
}