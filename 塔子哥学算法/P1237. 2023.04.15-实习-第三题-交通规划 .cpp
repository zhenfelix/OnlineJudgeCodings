// 题目内容

// 塔子哥所在的国家有 nn 个城市，这 nn 个城市排成一列，按顺序编号为 1,2,3,...,n1,2,3,...,n。然而，由于历史原因和地理条件等多种原因，这些城市之间并没有相互连接的铁路，导致交通十分不便。

// 为了改善这种情况，政府决定修建一些铁路来提高城市之间的交通效率。具体来说，政府计划在未来的 TT 天内进行一系列铁路建设工作。每一天，政府会进行如下操作之一：

//     L x：在编号为 xx 的城市和其左边的城市之间修建一条铁路，以便两个城市之间的交通更加便利。如果 xx 已经位于最左边，或者 xx 和它左边的城市之间已经存在铁路，则该操作无效。
//     R x：在编号为 xx 的城市和其右边的城市之间修建一条铁路，以便两个城市之间的交通更加便利。如果 xx 已经位于最右边，或者 xx 和它右边的城市之间已经存在铁路，则该操作无效。
//     Q x：查询从编号为 xx 的城市出发，最远能够到达的向左和向右的城市的编号。

// 塔子哥需要编写一段程序来模拟这一系列操作，并及时输出每个 Q x 操作的结果。通过这个程序，政府可以更加高效地规划城市之间的交通网络，从而促进经济和社会的发展。
// 输入描述

// 第一行输入两个正整数 nn ， TT ； 接下来 TT 行，每行输入形如题面中的其中一种。

// 1≤n≤100001≤n≤10000 ， 1≤T≤2001≤T≤200 ， 1≤x≤n1≤x≤n
// 输出描述

// 对于每一个Q x 操作，输出一行两个正整数，分别表示 xx 往左边和往右边最远能到达的城市编号中间用空格隔开。
// 样例

// 输入

// 3 5
// Q 2
// L 2
// Q 2
// R 2
// Q 2

// 输出

// 2 2
// 1 2
// 1 3


#include <bits/stdc++.h>
#include <functional>
#include <vector>
using namespace std;

int main() {
    int n,t;
    cin >> n >> t;
    vector<int> l(n),r(n);
    for (int i = 0; i < n; i++) l[i] = i, r[i] = i;
    function<int(int, vector<int>&)> find = [&] (int cur, vector<int> &parent) {
        if (parent[cur] != cur) parent[cur] = find(parent[cur], parent);
        return parent[cur];
    };
    while (t--) {
        char ch;
        int x;
        cin >> ch >> x;
        x--;
        if (ch == 'L') {
            if (x > 0 && l[x] == x) {
                l[x] = x-1;
                r[x-1] = x;
            }            
        }  
        else if (ch == 'R') {
            if (x < n-1 && r[x] == x) {
                l[x+1] = x;
                r[x] = x+1;
            }
        }
        else {
            cout << find(x,l)+1 << ' ' << find(x,r)+1 << endl;
        }
    }
    return 0;
}