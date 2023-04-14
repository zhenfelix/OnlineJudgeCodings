
// 2022.11.17-分奖金
// 题目描述

// 塔子哥最近做了一笔大生意，他想要给每位员工分配一些奖金，但是塔子哥不想直接发放给他们，他想通过游戏的方式来决定每个人分多少钱。

// 按照员工的工号顺序，每个人随机抽取一个数字。按照工号的顺序往后排列，遇到第一个数字比自己数字大的，那么，前面的员工就可以获得“距离数字差值”的奖金。如果遇不到比自己数字大的，就给自己分配随机数数量的奖金。

// 例如，按照工号顺序的随机数字是：2,10,3。那么第2个员工的数字10比第1个员工的数字2大，所以，第1个员工可以获得 1×（10−2）=81×（10−2）=8 。第2个员工后面没有比他数字更大的员工，所以，他获得他分配的随机数数量的奖金，就是10。第3个员工是最后一个员工，后面也没有比他更大数字的员工，所以他得到的奖金是3。

// 塔子哥现在忙于他的另外一笔大生意，请问你能帮他计算一下每位员工最终分到的奖金都是多少钱吗？
// 输入描述

// 第一行n表示员工数量（包含最后一个老板） (2 <= n <= 1e5)

// 第二是每位员工分配的随机int型整数
// 输出描述

// 最终每位员工分到的奖金数量
// 样例

// 输入

// 3
// 2 10 3

// 输出

// 8 10 3


#include<bits/stdc++.h>

using namespace std;
using ll = long long;

using pii = pair<int,int>;
using tiii = tuple<int,int,int>;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("contests/input", "r", stdin);
    
    int n, num, x;
    char ch;
    const int inf = 0x3f3f3f3f;
    cin >> n;
    vector<ll> arr(n);
    vector<int> st;
    for (int i = 0; i < n; i++){
       cin >> arr[i];
       while (!st.empty() && arr[st.back()] < arr[i])
       {
        int j = st.back();
        arr[j] = (arr[i]-arr[j])*(i-j);
        st.pop_back();
       }
       st.push_back(i);
    }
    for (int i = 0; i < n; i++) {
        cout << arr[i];
        if (i < n-1) cout << " ";
        else cout << endl;
    }
    return 0;
}