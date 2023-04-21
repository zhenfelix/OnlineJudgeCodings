
// 2023.3.16-组装电脑
// 题目内容

// 塔子哥是一位电脑发烧友，热爱DIY组装电脑。他研究了各种零部件，了解到不同型号的零件有不同的性能和价格，而性价比也会有所差异。因此，他需要谨慎地选择零部件，以使他的电脑既具有出色的性能，又不会让他花费太多的钱。

// 这一次，塔子哥决定升级他的电脑，需要购买nn个零件，每个零件有多个型号可供选择。他知道每个型号的价格 aiai​ 和性能 vivi​ ，并且他有一个限制条件，塔子哥需要每个零件选择一个型号并且总价格不能超过xx元。他希望在这个限制条件下，选出的零件能够使他的电脑性能尽可能强大。塔子哥需要你的帮助，来找到最优的选择方案。
// 输入描述

// 第一行输入两个正整数 nn 和 xx ，代表电脑的零件数量以及塔子哥最大的预算。

// 接下来的 3∗n3∗n 行，每三行用来描述一个零件的不同型号的价格和性能。

// 对于每个零件，第一行输入一个正数 mm ，代表该零件有多少种型号。

// 1≤n,m≤401≤n,m≤40

// 1≤ai,vi,x≤1091≤ai​,vi​,x≤109

// 保证所有 mm 之和不超过 4040 ，即所有零件的型号数量之和不超过 4040 种。
// 输出描述

// 如果无法完成组装，则直接输出−1。−1。 否则输出一个正整数，代表最终最大的性能。
// 样例11

// 输入

// 2 3
// 2
// 1 3
// 2 5
// 2
// 2 3
// 2 4

// 输出

// 4

// 说明： 一共需要两个零件。 第一个零件选择第一个型号，第二个零件也选择第一个型号。 这样总价格为 33 ，总性能为 44 。


#include<bits/stdc++.h>
using namespace std;
using ll = long long;
int main() {
    // freopen("contests/input","r",stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n,x;
    cin >> n >> x;
    ll ans = -1;
    vector<vector<int>> cost(n), performance(n);
    for (int i = 0; i < n; i++) {
        int m;
        cin >> m;
        cost[i].resize(m);
        performance[i].resize(m);
        for (int j = 0; j < m; j++) cin >> cost[i][j];
        for (int j = 0; j < m; j++) cin >> performance[i][j];
    }
    function<void(int,int,ll)> dfs = [&] (int i, int r, ll p) {
        if (r < 0) return;
        if (i == n) {
            ans = max(ans,p);
            return;
        }
        int m = cost[i].size();
        for (int j = 0; j < m; j++) dfs(i+1,r-cost[i][j],p+performance[i][j]);
        return;
    };
    dfs(0,x,0);
    cout << ans << endl;
    return 0;
}