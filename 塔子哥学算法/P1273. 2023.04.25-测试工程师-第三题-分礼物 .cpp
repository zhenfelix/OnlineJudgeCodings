// 题目内容

// 塔子哥是一位热心的数学老师，他每年都会给他的学生们准备一些有趣的数学问题，作为圣诞节的礼物。今年，他准备了 nn 件无差别的小礼物，比如钢笔、橡皮、尺子等。他想要正常分给他的 kk 个学生，，并且不会有剩余的礼物。

// 但是塔子哥有点困惑，因为他不知道如何分配这些礼物。他想到了你，他的助教，也是一位数学高手。他决定把这个问题交给你，希望你能帮他找到一个能够将 nn 个无差别的礼物分给 kk 个学生的分法。
// 输入描述

// 输入仅一行，包含两个整数 nn 和 kk ， nn 表示礼物的数量， kk 表示小朋友的数量。（ 0≤n≤100≤n≤10 ， 1≤k≤101≤k≤10 ）
// 输出描述

// 第一行输出分法总数 tt 。

// 后续 tt 行依次列出每种分法，每件礼物用字符 * (ascii码为 4242 )表示，用字符 | (ascii码为 124124 ) 分隔小朋友。

// 具体输出和顺序请参考样例。
// 样例

// 输入

// 3 2

// 输出

// 4
// ***|
// **|*
// *|**
// |***

// 样例解释

// 第一行表示 33 件礼物分给 22 个小朋友的分法一些有 44 种；

// 第二行表示第一个小朋友分有 33 件礼物，第二个小朋友无礼物，以 | 分隔；

// 第三行表示第一个小朋友分有 22 件礼物，第二小朋友分有 11 件礼物，以 | 分隔；

// 第四行表示第一个小朋友分有 11 件礼物，第二个小朋友分有 22 件礼物，以 | 分隔；

// 第五行表示第一个小朋友无礼物，第二小朋友分有 33 件礼物，以 | 分隔。


#include <bits/stdc++.h>
#include <functional>
using namespace std;

int main() {
    int n, g;
    cin >> n >> g;
    --g;
    vector<string> ans;
    function<void(int,int,int,string)> dfs = [&] (int i, int nn, int gg, string path) {
        if (i == n+g) {
            ans.push_back(path);
            return;
        }
        if (nn) {
            path.push_back('*');
            dfs(i+1,nn-1,gg,path);
            path.pop_back();
        }
        if (gg) {
            path.push_back('|');
            dfs(i+1,nn,gg-1,path);
            path.pop_back();
        }
        return;
    };
    string tmp;
    dfs(0,n,g,tmp);
    cout << ans.size() << endl;
    for (auto &s : ans) cout << s << endl;
    return 0;
}