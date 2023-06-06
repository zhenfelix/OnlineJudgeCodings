// 题目内容

// 热门手游Y又迎来了大版本更新了，这次出了新的副本。这次副本中新增了 NN 个任务，每一个任务都需要花费一个单位时间，每个任务都有自己的截至时间和获得固定的佣金。

// 塔子哥从 11 时刻开始开启副本，将持续在线玩 109109个单位时间。在任一时刻，塔子哥都可以选择编号 11 到 NN 的 NN 个任务中的任意一个任务来完成。 由于塔子哥在每个单位时间里只能做 11 个任务，而每个任务都有一个截止日期。所以塔子哥可能不得不放弃一些任务来尽可能地获得最大的佣金。

// 对于第 ii 个任务，有一个截止时间DiDi​，如果塔子哥可以完成这个订单，那么他可以获的 PiPi​ 个佣金。 塔子哥想尽可能地获取更多的佣金来购买更高级的装备，那么塔子哥该选择做哪些任务才能得到更多的佣金呢？
// 输入描述

// 第 11 行包含一个整数 NN。 (11 <= NN <= 5×1055×105)

// 接下来有 NN 行，每行包含两个以空格分隔的整数DiDi​和PiPi​ 。(11 <= DiDi​ <=<=109109，11 <= PiPi​ <=<=109109)
// 输出描述

// 一行，包含一个整数，表示塔子哥所能拿到的最多佣金。
// 样例1

// 输入

// 4
// 2 10
// 1 5
// 1 7
// 3 20

// 输出

// 37

// 说明

// Complete job 3 (1,7) at time 1 and complete job 1 (2,10) at time 2 and complete job 4 (3,20) at time 3 to maximize the earnings (7 + 10 + 20 -> 37).

// 样例2

// 输入

// 5
// 2 2
// 4 3
// 1 1
// 3 2
// 3 2

// 输出

// 9
#include <bits/stdc++.h>
#include <queue>
using namespace std;

using pii = pair<int,int>;
using ll = long long;

int main() {
    int n;
    cin >> n;
    vector<pii> arr;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        arr.push_back({a,b});
    }
    sort(arr.begin(), arr.end());
    priority_queue<int,vector<int>,greater<>> pq;
    ll ans = 0;
    for (int i = 0; i < n; i++) {
        auto [t,v] = arr[i];
        ans += v;
        pq.push(v);
        if (t < pq.size()) {
            ans -= pq.top();
            pq.pop();
        }
    }
    cout << ans << endl;
    return 0;
}