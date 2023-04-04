
// 内推笔试-2023.2.22.投喂珍珠
// 介绍

// 根据群友的描述，这是一场pdd内推的笔试。参加的人数少，但是难度不低

// 题目内容

// 塔子哥生活在美丽的华光林，他非常喜欢这里的环境和氛围。在平常的休息时间，他会在家附近散步，欣赏美景，感受大自然的魅力。顺便会投喂经过遇到的小马们，让它们感受到人类的温暖和关爱。这样的生活让他感到非常满足和幸福。已知华光林共有 NN 个广场(分别编号 11 ~ NN ，塔子哥住在 11 号广场)，以及有 N−1N−1 条道路，保证广场两两之间相互连通，且只有唯一一条通路， 且已知第 ii 个广场有 AiAi​ 只马。

// 塔子哥平时散步的时候有以下这些习惯：

//     任意一个广场不能两次访问
//     塔子哥的背包只能装下最多MM份马粮
//     11 份马粮只能投喂 11 只马
//     若要经过某个广场则要投喂其中所有的马(^. w .^)

// 塔子哥想知道，应当如何选择路线使得能投喂到最多数量的广场，且需要的马粮数量最少。
// 输入描述

// 第一行，两个整数 NN 和 MM ，分别表示华光林广场的数量，和准备带出门的马粮的份数( 1≤N≤50,0001≤N≤50,000 ， 0≤M≤5,000,0000≤M≤5,000,000 )

// 第二行，共 NN 个整数，其中第 ii 个整数 AiAi​ 表示第 ii 个广场的马的数量。( 0≤Ai≤1000≤Ai​≤100 )

// 接下来 N−1N−1 行，每行两个整数 XX 和 YY ，表示编号 XX 和 YY 的广场之间存在一条道路。( 1≤X,Y≤N1≤X,Y≤N )
// 输出描述

// 共一行，两个整数，分别表示：能投喂最多数量的广场，以及在此情况下需要最少多少马粮。
// 样例
// 样例一：

// 输入

// 2 1
// 2 1
// 1 2

// 输出

// 0 0

// 样例解释

// 塔子哥只有 11 份马粮，小于 11 号广场的马马数量，因此塔子哥决定不出门喂马。(T V T)

// 没有任何一个广场的马咪被投喂，也就不需要任何马粮。
// 样例二：

// 输入

// 3 4
// 1 2 3
// 1 2
// 2 3

// 输出

// 2 3


#include<bits/stdc++.h>

using namespace std;
using ll = long long;

using pii = pair<int,int>;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("contests/input", "r", stdin);
    
    int n, tot;
    cin >> n >> tot;
    vector<int> arr(n);
    vector<vector<int>> g(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < n-1; i++){
        int u, v;
        cin >> u >> v;
        g[u-1].push_back(v-1);
        g[v-1].push_back(u-1);
    }
    vector<int> ans(2,0);
    function<void(int,int,int,int)> dfs = [&] (int cur, int parent, int cnt, int cost) {
        cnt++;
        cost += arr[cur];
        if (cost > tot) return;
        if (cnt > ans[0] || (cnt == ans[0] && cost < ans[1])) ans = {cnt,cost};
        for (auto nxt : g[cur]) {
            if (nxt == parent) continue;
            dfs(nxt,cur,cnt,cost);
        }
    };
    dfs(0,0,0,0);
    cout << ans[0] << " " << ans[1] << endl;
    
    return 0;
}