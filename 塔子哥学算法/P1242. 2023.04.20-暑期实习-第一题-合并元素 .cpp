// 题目内容

// 曾经有一位叫做塔子哥的小伙子，他是一位有着非常高超数学技能的年轻人，对于算术和几何学方面非常着迷。有一天，他得到了一个由 nn 个整数构成的数组。但是他很快发现这个数组非常不平衡，有些元素太大而有些元素太小，于是他想进行一次操作，使得数组变得更加平衡。

// 他的操作非常简单：他可以选择两个相邻的元素，将它们合并成一个元素，新元素的值等于原来两个元素的和。但是他只能进行一次这样的操作。

// 他决定利用他的数学技能，找到可以让数组变得最平衡的方法。

// 他定义数组的极差为数组的最大值减去最小值。他的目标是使得操作后数组的极差尽可能的小，你能帮塔子哥解决吗？
// 输入描述

// 输入第一行为一个整数 nn ，表示数组的长度。

// 输入第二行为 nn 个整数，第 ii 个整数为 aiai​ 。

// 2≤n≤1052≤n≤105， 1≤ai≤1091≤ai​≤109
// 输出描述

// 一个整数，代表操作后的极差最小值。
// 样例

// 输入

// 3
// 1 4 5

// 输出

// 0


#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<int> mx(n), mi(n);
    mx[0] = mi[0] = arr[0];
    for (int i = 1; i < n; i++) {
        mx[i] = max(mx[i-1],arr[i]);
        mi[i] = min(mi[i-1],arr[i]);
    }
    int ans = n == 2 ? 0 : max(mx[n-3],arr[n-2]+arr[n-1])-min(mi[n-3],arr[n-2]+arr[n-1]);
    int cmi = arr[n-1], cmx = arr[n-1];
    for (int i = n-4; i >= 0; i--) {
        ans = min(ans, max(arr[i+1]+arr[i+2],max(mx[i],cmx))-min(arr[i+1]+arr[i+2],min(mi[i],cmi)));
        cmi = min(cmi,arr[i+2]);
        cmx = max(cmx,arr[i+2]);
    }
    ans = min(ans, max(arr[0]+arr[1],cmx)-min(arr[0]+arr[1],cmi));
    cout << ans << endl;
}