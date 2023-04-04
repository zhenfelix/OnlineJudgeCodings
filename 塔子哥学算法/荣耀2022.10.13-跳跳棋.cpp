
// 2022.10.13-跳跳棋
// 题目内容

// 在某个遥远的国度里，有一种传统的游戏叫做“跳跳棋”，这是一种基于积分的游戏。在这个国度里，跳跳棋已经有着悠久的历史，并且已经被许多人认为是一种智力和策略的游戏。人们在跳跳棋中可以锻炼自己的思维和判断能力。因此，这个游戏非常受欢迎，人们经常在闲暇时间里玩这个游戏。

// 传统的跳跳棋棋盘呈直线状，共有 NN 格，起始位置和结束位置都在棋盘之外。每一格都对应一个不同的积分值，而每次跳跃都必须跳过一个或多个格子，而且不允许跳到相邻的格子上，也不可以回跳，游戏的目标是通过跳跃来获取最高的积分。
// 输入描述

// 第一行为整数 NN ,表示跳棋格数 (1≤N≤100000)(1≤N≤100000)

// 第二行为每一格代表的分数 MM (1≤M≤1000)(1≤M≤1000)
// 输出描述

// 能获得的最高积分
// 样例

// 输入

// 3
// 1 5 2

// 输出

// 5


#include<bits/stdc++.h>

using namespace std;
using ll = long long;

using pii = pair<int,int>;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("contests/input", "r", stdin);
    int n,x,cur = 0, pre = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        x = max(x+pre,cur);
        pre = cur;
        cur = x;
    }
    cout << cur << endl;
    
    return 0;
}