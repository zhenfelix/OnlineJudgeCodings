// 题目内容

// 塔子哥是一个收藏家，他喜欢收集各种珍奇的物品。最近，他在旅游时在俄罗斯购买了一些俄罗斯套娃。他深深地被这些绚丽多彩的小玩意吸引住了，每天都会花费大量的时间玩弄它们。随着时间的推移，他逐渐发现将套娃放在其他套娃内是一个有趣的游戏，并决定挑战自己，看看他是否能以最小的成本套上所有的俄罗斯套娃。

// 具体的，塔子哥有 nn 个俄罗斯套娃，第 ii 个俄罗斯套娃的大小为 aiai​ ，内部空间为 bibi​ ( bi≤aibi​≤ai​ )和一个价值 cici​ 。

// 对于两个俄罗斯套娃 xx 和 yy ， xx 能放入 yy 中当且仅当 ax≤byax​≤by​ ，且放入后会占据 yy 大小为 axax​ 的内部空间，即y 的内部空间剩下 by−axby​−ax​ ，每个俄罗斯套娃只能放在另外的一个俄罗斯套娃内，每个俄罗斯套娃内部也只能放一个俄罗斯套娃(当然内部放的这个俄罗斯套娃可以内部还有俄罗斯套娃)。

// 显然俄罗斯套娃是套的越多越好，如果套完之后俄罗斯套娃 ii 还剩 kk 的内部空间塔子哥需要付出 ci×kci​×k 的花费，总花费为所有俄罗斯套娃的花费之和。

// 现在塔子哥想知道最小的花费为多少？
// 输入描述

// 第一行一个正整数 nn ，表示俄罗斯套娃的个数

// 接下来三行每行 nn 个整数，分别为

// a1,a2,...,an
// b1,b2,...,bn
// c1,c2,...,cn

// 1≤n,ai,bi,ci≤1000001≤n,ai​,bi​,ci​≤100000 ， bi≤aibi​≤ai​
// 输出描述

// 输出一个整数表示最小的花费。
// 样例

// 输入

// 3
// 5 4 3
// 4 2 2
// 3 2 1

// 输出

// 6

// 样例解释

// 将第二个俄罗斯套娃放在第一个里面，第三个不动，这样第一个俄罗斯套娃剩 00 的空间，第二个剩 22 ，第三个剩 22 。总花费为 0∗3+2∗2+2∗1=60∗3+2∗2+2∗1=6 。

// 可以证明这是花费最小的方案。

#include <bits/stdc++.h>
#include <queue>
#include <vector>
using namespace std;
using ll = long long;
using pii = pair<int,int>;
int main() {
    int n;
    ll ans = 0;
    cin >> n;
    vector<int> arr(n), brr(n), crr(n), idx(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < n; i++) cin >> brr[i];
    for (int i = 0; i < n; i++) {
        cin >> crr[i];
        ans += (ll)crr[i]*brr[i];
    }
    for (int i = 0; i < n; i++) idx[i] = i;
    sort(idx.begin(), idx.end(), [&](int a, int b) {
        return arr[a] > arr[b];
    });
    priority_queue<pii,vector<pii>> pq, candidates;
    for (auto i : idx) {
        while (!pq.empty() && pq.top().first >= arr[i]) {
            auto [b,j] = pq.top();
            pq.pop();
            candidates.push({crr[j],j});
        }
        if (!candidates.empty()) {
            auto [c,j] = candidates.top();
            candidates.pop();
            ans -= (ll)arr[i]*c;
        }
        pq.push({brr[i],i});
    }
    cout << ans << endl;
    return 0;

}