#include <iostream>
#include<cstring>
#include<cmath>
using namespace std;
int x[256]={0},y[256]={0};
char str[100005];
int main() {
//    freopen("input.txt", "r", stdin);
    for(char ch='A';ch<='Z';ch++){
        if(ch>='A'&&ch<='C')x[ch]=1,y[ch]=2;
        else if(ch>='D'&&ch<='F')x[ch]=1,y[ch]=3;
        else if(ch>='G'&&ch<='I')x[ch]=2,y[ch]=1;
        else if(ch>='J'&&ch<='L')x[ch]=2,y[ch]=2;
        else if(ch>='M'&&ch<='O')x[ch]=2,y[ch]=3;
        else if(ch>='P'&&ch<='S')x[ch]=3,y[ch]=1;
        else if(ch>='T'&&ch<='V')x[ch]=3,y[ch]=2;
        else if(ch>='W'&&ch<='Z')x[ch]=3,y[ch]=3;
    }
    int t;
    scanf("%d",&t);
    while(t--){
        scanf("%s",str);
        int len=strlen(str);
        int ans=0,tx_p=1,ty_p=1,tx,ty;
        for(int i=0;i<len;i++){
            tx=x[str[i]],ty=y[str[i]];
            ans+=(abs(tx-tx_p)+abs(ty-ty_p));
            tx_p=tx,ty_p=ty;
        }
        printf("%d\n",ans);
    }
    return 0;
}

// 题目描述
//     小美想要在电视上看电影，我们知道在电视上搜索电影可以通过搜索电影名字首字母缩写得到，通过首字母搜索电影的界面由一个九宫格组成，如下图：

// @!:
    

// ABC
    

// DEF

// GHI
    

// JKL
    

// MNO

// PQRS
    

// TUV
    

// WXYZ

//     光标初始在这个九宫格的左上方，也就是在 “@!:”的位置，每次小美想要输入一个字母，需要通过不断地按上下左右四个方向键(并且只能按方向键），把光标从当前所在的格子移动到目标的格子(也就是待输入的字母所在的格子)，然后在目标的格子上通过其他的按键来输入字母。小美觉得频繁地按方向键是十分烦人的事情，所以她想设计一种移动光标方案使得方向键按的次数最少。问最少要几次?
//     小美想看 T 部电影，所以她会问你 T 个电影名字的缩写分别需要多少次输入。
//     注意在一个电影名字输入完以后，光标会回到左上角，期间按的方向键不会计入答案。

// 输入描述:

// 第一行一个T(T ≤ 10)，表示小美想看的电影数。
// 接下来 T 行，每行一个长度不超过100,000的字符串，表示一部电影名字的缩写，保证缩写的每个字符都是大写英文字母。

// 输出描述:

// 对于每个电影名字缩写，输出输入这个名字的最小按方向键的次数。

// 示例1
// 输入

// 2
// AA
// AT

// 输出

// 1
3