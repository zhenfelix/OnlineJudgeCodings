
// 塔子哥の插队
// 题目内容

// 塔子哥要去学校接他的弟弟，但是他不想排队。他发现学校的学生放学回家有五个优先级，学习成绩越好回家时间越快，1 表示学习成绩最好，5 表示学习成绩最差。

// 现在他知道如果他弟弟是当前学习成绩最好的学生，那么他可以插队到其他人前面去接他弟弟。

// 给定一个学生的编号和他的学习成绩的时间表，输出每次被接回家的学生时的学生编号。

// 如果有多个同级优先级的学生，按照到达顺序被接回家。
// 输入描述

// 输入第一行是一个正整数 nn ,表示输入的序列中的事件数量。(1≤n≤5001≤n≤500)

// 接下来有 nn 行，每行第一个字符为 aa 或 pp 。

// 当字符为 aa 时，后面会有两个的正整数 numnum 和 xx ,表示到来的学生编号为 numnum ,学习成绩为 xx ;

// 当字符为 pp 时，表示当前学习成绩优先级最高的学生被接回家。
// 输出描述

// 输出包含若干行，对于每个 pp ， 输出一行，仅包含一个正整数 numnum , 表示学习成绩最好的学生被接回家的学生的编号。
// 样例

// 输入

// 4
// a 1 3
// a 2 2
// a 3 2
// p

// 输出

// 2


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
    priority_queue<tiii,vector<tiii>,greater<>> pq;
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> ch;
        if (ch ==  'a') {
            cin >> num >> x;
            pq.push({x,i,num});
        }
        else {
            auto [x_,j,idx] = pq.top();
            pq.pop();
            cout << idx << endl;
        }
    }
    return 0;
}