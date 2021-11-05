// https://cses.fi/problemset/task/2426/

#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using pii = pair<int,int>;

const int maxn = 2e5+10;

pii arr[maxn];
ll lo[maxn], hi[maxn];
int n, a, b;



void solve(){
    ll res = 0, sleft = 0;
    priority_queue<int, vector<int>, greater<>> mxq;
    sort(arr, arr+n, greater<>());
    for (int i = 0; i < a+b; i++){
        auto [x,y] = arr[i];
        sleft += y;
        sleft += (x-y);
        mxq.push(x-y);
        if (mxq.size() > a){
            sleft -= mxq.top();
            mxq.pop();
        }
        lo[i] = sleft;
    }
    ll sright = 0;
    priority_queue<int, vector<int>> miq;
    for (int i = n-1; i >= a; i--){
        auto [x,y] = arr[i];
        miq.push(y);
        if (miq.size() > n-a-b){
            sright += miq.top();
            miq.pop();
        }
        hi[i] = sright;
    }
    for (int i = a-1; i < a+b; i++){
        res = max(res, lo[i]+(i < n ? hi[i+1] : 0));
    }
    cout << res << endl;
}

int main()
{
    // freopen("input", "r", stdin);
    int x, y;
    cin >> a >> b >> n ;
    for (int i = 0; i < n; i++){
        cin >> x >> y;
        arr[i] = {x,y};
    }
    solve();
}
