
// 2023.2.22-爬山
// 题目内容

// 塔子哥是一个热爱户外运动的人，他周末经常约朋友一起登山。华光林山清水秀，景色宜人，让他感到非常愉悦。他喜欢在登山的过程中欣赏美景，感受大自然的魅力。同时，他也喜欢挑战自己，尝试攀登更高的山峰。

// 塔子哥登山时每一步可以选择向上爬一个台阶或者多个台阶，如果登山时选择的台阶不同，则为一种爬山方案。

// 塔子哥想知道，华光林的每座山各有多少种不同的爬山方案(输出结果对 109+7109+7 取模)。
// 输入描述

// 第一行，三个整数 NN 、 PP 和 KK 分别代表山的个数 NN ，塔子哥一次最高能爬的高度 PP 以及塔子哥一次最多能跨越的台阶数 KK 。

// ( 1≤N≤101≤N≤10 ， 1≤P≤1,0001≤P≤1,000 ， 1≤K≤1,0001≤K≤1,000 )

// 接下来 NN 行，每行的第一个整数 MiMi​ 表示第 ii 座山一共有 MiMi​ 个台阶，接下来有 MiMi​ 个整数，分别表示每个台阶的高度 HjHj​

// ( 1≤Mi≤10,000,1≤Hj≤1,0001≤Mi​≤10,000,1≤Hj​≤1,000)。
// 输出描述

// 输出 NN 行，每行一个整数，表示第 ii 座山塔子哥可以选择的登山方案数目。
// 样例
// 样例一：

// 输入

// 3 3 2
// 4 1 1 1 1
// 4 2 2 2 2
// 5 2 2 2 3 4

// 输出

// 5
// 1
// 0

// 备注

// 如果某一台阶 HjHj​ 的高度超过了塔子哥次能爬的高度 PP ， 那塔子哥就不会选择这爬座山， 登山方案数为 00 。


#include<bits/stdc++.h>

using namespace std;
using ll = long long;

using pii = pair<int,int>;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("contests/input", "r", stdin);
    const int MOD = 1e9+7;
    int t,p,k;
    cin >> t >> p >> k;
    while (t--)
    {
        int m;
        cin >> m;
        vector<int> arr(m);
        for (int i = 0; i < m; i++) cin >> arr[i];
        vector<int> dp(m+1);
        dp[0] = 1;
        int h = 0, cs = 1, j = 0;
        for (int i = 1; i <= m; i++){
            h += arr[i-1];
            while (h > p || i-j > k)
            {
                cs = (cs+MOD-dp[j])%MOD; 
                h -= arr[j];
                j++;
            }
            dp[i] = cs;
            cs = (cs+cs)%MOD;
        }
        cout << dp[m] << endl;
    }
    
    
    return 0;
}