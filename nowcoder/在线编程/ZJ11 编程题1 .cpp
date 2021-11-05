// #include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>

using namespace std;
using ll = long long;
using pii = pair<int,int>;

const int inf = 0x3f3f3f3f;
int n, x, y;



void solve(){
    // cin >> n;
    scanf("%d", &n);
    vector<pii> positions(n);
    for (int i = 0; i < n; i++){
        // cin >> x >> y;
        scanf("%d%d", &x, &y);
        positions.push_back({x,y});
    }
    sort(positions.begin(), positions.end(), greater<pii>());
    vector<pii> res;
    int cy = -inf;
    for (auto [x,y] : positions){
        if (y > cy){
            res.push_back({x,y});
            cy = y;
        }
    }
    while (!res.empty()){
        auto [x,y] = res.back();
        res.pop_back();
        // cout << x << " " << y << endl;
        printf("%d %d\n", x, y);
    }
}

int main()
{
//     freopen("input", "r", stdin);
    // cin >> t;
    
    // for (int i = 1; i <= t; i++){
    //     cout << "Case #" << i << ": ";
    //     solve();
    // }
    solve();
}


// // #include <bits/stdc++.h>
// #include <vector>
// #include <algorithm>
// #include <climits>
// #include <iostream>
// #include <unordered_map>

// using namespace std;
// using ll = long long;
// using pii = pair<int,int>;

// const int inf = 0x3f3f3f3f;
// int n, x, y;



// void solve(){
//     cin >> n;
//     vector<pii> positions(n);
//     for (int i = 0; i < n; i++){
//         cin >> x >> y;
//         positions.push_back({x,y});
//     }
//     sort(positions.begin(), positions.end(), greater<pii>());
//     vector<pii> res;
//     int cy = -inf;
//     for (auto [x,y] : positions){
//         if (y > cy){
//             res.push_back({x,y});
//             cy = y;
//         }
//     }
//     while (!res.empty()){
//         auto [x,y] = res.back();
//         res.pop_back();
//         cout << x << " " << y << endl;
//     }
// }

// int main()
// {
//     // freopen("input", "r", stdin);
//     // cin >> t;
    
//     // for (int i = 1; i <= t; i++){
//     //     cout << "Case #" << i << ": ";
//     //     solve();
//     // }
//     ios::sync_with_stdio(false);
//     solve();
// }
