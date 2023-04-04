
2022.9.11-最佳爬楼方案
题目大意

有个神奇楼梯，每次可以传送不超过 kk 个楼梯，而每次爬楼花费的体力为 max(0,目标楼梯高度−当前楼梯高度)max(0,目标楼梯高度−当前楼梯高度) .

现在塔子哥想知道求从第一个楼梯到最后一个楼梯的最小花费是多少。
输入描述

第一行输入n,kn,k，代表楼梯的阶数和最多能传送跨过多少个楼梯。

第二行nn个数，代表每座楼梯的高度
样例

输入

7 4
12 38 14 71 31 61 33

输出

21

数据范围

1≤k≤n≤40001≤k≤n≤4000

#include<bits/stdc++.h>

using namespace std;
using ll = long long;

using pii = pair<int,int>;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("contests/input", "r", stdin);
    
    int n, k;
    const int inf = 0x3f3f3f3f;
    cin >> n >> k;
    vector<int> arr(n,0),dp(n,inf);
    dp[0] = 0;
    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 1; i < n; i++){
        for (int j = max(0,i-k); j < i; j++){
            dp[i] = min(dp[i], max(0,arr[i]-arr[j])+dp[j]);
        }
    }
    cout << dp[n-1] << endl;
    return 0;
}