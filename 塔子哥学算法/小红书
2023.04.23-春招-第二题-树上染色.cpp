
// 2023.04.23-春招-第二题-树上染色
// 题目内容

// 塔子哥是一个喜欢画画的小朋友，他有一本画册，里面有很多空白的树形图案，每个图案都有 nn 个节点，用线段连接起来。

// 有一天，塔子哥拿出一支红色的彩笔，想给画册里的树形图案涂色。他随机地选择了一些节点，用红色的彩笔把它们涂满。

// 这样，画册里的树形图案就变成了一些红色和白色的节点组成的图案。

// 塔子哥认为，如果两个红色的节点之间有一条或多条线段相连，那么它们就属于同一个红色连通块。

// 塔子哥想知道，所有的红色连通块中，第 k 大的连通块有多少个节点？
// 输入描述

// 第一行输入为两个正整数 nn 和 kk 。

// 第二行输入为一个长度为 nn 的字符串，第 ii 个字符为 R 代表号节点被染成红色，为 W 代表未被染色。

// 接下来的 n−1n−1 行，每行输入两个正整数 uu 和 vv ，代表节点 uu 和节点 vv 有一条边连接。

// 保证输入的数据能构成一棵树。

// 1≤k≤n≤1051≤k≤n≤105 ， 1≤u,v≤n1≤u,v≤n
// 输出描述

// 如果红色连通块的数量小于 kk ，则输出 −1−1 。

// 否则输出一个正整数，代表第 kk 大的红色连通块的节点数。(大小相同的连通块不用去重)
// 样例1

// 输入

// 5 2
// WWRRW
// 1 2
// 1 4
// 1 5
// 2 3

// 输出

// 1

// 样例2

// 输入

// 5 2
// RRRRR
// 1 2
// 1 4
// 1 5
// 2 3

// 输出

// -1


#include<bits/stdc++.h>
using namespace std;

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int n, k;
    cin >> n >> k;
    string s;
    cin >> s;
    vector<int> parent(n);
    for (int i = 0; i < n; i++) parent[i] = i;
    function<int(int)> find = [&] (int cur) {
        int p = cur;
        while (parent[p] != p) p = parent[p];
        while (parent[cur] != p) {
            int nxt = parent[cur];
            parent[cur] = p;
            cur = nxt;
        }
        return p;
    };
    function<void(int,int)> connect = [&] (int u, int v) {
        int ru = find(u), rv = find(v);
        if (ru != rv) parent[ru] = rv;
        return; 
    };
    for (int i = 0; i < n-1; i++) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        if (s[u] == 'R' && s[v] == 'R') connect(u,v);
    }
    vector<int> cnt(n,0);
    for (int i = 0; i < n; i++) {
        if (s[i] == 'R') cnt[find(i)]++;
    }
    vector<int> arr;
    for (int i = 0; i < n; i++) {
        if (cnt[i] > 0) arr.push_back(cnt[i]);
    }
    if (k > arr.size()) {
        cout << -1 << endl;
        return 0;
    }
    sort(arr.begin(), arr.end(), greater{});
    cout << arr[k-1] << endl;
    return 0;

};