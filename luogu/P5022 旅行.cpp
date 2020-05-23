// https://www.luogu.com.cn/blog/CJYblog/p5022-lv-xing-ti-xie

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <iostream>
//#include<bits/stdc++.h>//万能头
using namespace std;

const int MAXN = 5000 + 10;//定义常量

int n,m,cur;//n、m与题目相对应，cur记录答案累加用途
int in_out[MAXN],ans[MAXN];//ans为答案，in_out为度数（即入读加上出度）
int res[MAXN];//用于临时存目前计划，在更新ans与res判断


vector<int>nei[MAXN];//动态数组用于记录邻居，这里用于优化时间复杂度
bool dis[MAXN][MAXN];//邻接矩阵，用来优化判断两个点的边目前又没有删
struct Line{//记录边的结构体
    int xx,yy;//起始点和终止点
}line[MAXN];

bool b[MAXN],use[MAXN];//b用于在DFS时看是否搜过了 ,use记录该店是否在环内

inline int read(){//读入优化
    int f = 1, x = 0;
    char c = getchar();

    while (c < '0' || c > '9')
    {
        if (c == '-')
            f = -1;
        c = getchar();
    }

    while (c >= '0' && c <= '9')
    {
        x = x * 10 + c - '0';
        c = getchar();
    }

    return f * x;
}

void init(){//读入函数
    n = read(),m = read();//读入点和边

    for(int i = 1;i <= m; i++){//读入边
        int x = read(),y = read();
        dis[x][y] = dis[y][x] = true;//将x与y的邻接矩阵更新
        nei[x].push_back(y);//将y压入x的邻居
        nei[y].push_back(x);//将x压入y的邻居
        in_out[x]++,in_out[y]++;//将x和y的度数++
        line[i] = (Line){x,y};//保存边
    }
    
    //for(int i = 1;i <= n; i++){
    //  for(int j = 1;j <= n; j++){
    //      cout<<dis[i][j]<<" ";
    //  }
    //  cout<<endl;
    //}
    //调试函数
    
    return;
}

void out(){//输出函数，单独拿出来是用于调试用的
    for(int i = 1;i <= n; i++){
        cout<<ans[i]<<" "; //循环输出答案
    }
    cout<<"\n";
    return;
}

void new_ans(){//更新答案
    for(int i = 1;i <= n; i++){
        ans[i] = res[i];
    }
}

void work() {//用于判断目前方案与答案哪个更优
    if(ans[1] == 0){//如果目前答案为空，直接记录
        new_ans();//更新答案
        //out();
        return;//这里一定要返回
    }

    for(int i = 1; i <= n; i++) {//逐次比较哪个更优
        if(res[i] == ans[i])//如果相同则继续
            continue;
        else if(res[i] < ans[i]) {//当前方案更优
            new_ans();//更新
            //out();
            return;
        }
    //  out();
        
        return;
    }
}

void Topo(){//基环图(与拓扑排序差不多)
    queue<int>q;//定义队列
    
    for(int i = 1;i <= n; i++){//将度数为1的雅图队列
        if(in_out[i] == 1){
            q.push(i);
            use[i] = true;//标记不在环中
        }
    }
    
    while(!q.empty()){//还可以继续做
        int tot = q.front();//取队首
        int len = nei[tot].size();
        
        q.pop();
        // use[tot] = true;//标记不在环中
        
        for(int i = 0;i < len; i++){//依次删除度数
            int next = nei[tot][i];//下一个点
            in_out[next]--;
            
            if(in_out[next] == 1){//压入队列
                q.push(next);
                use[next] = true;
            }
        }
    }
}

void dfs_plan_1(int now){//用于情况二的DFS，这里不要回溯
    ans[++cur] = now;//直接更新答案
    b[now] = true;//标记
    int len = nei[now].size();
    
    for(int i = 0;i < len; i++){//循环
        int next = nei[now][i];
     
        if(b[next])continue;
        if(!dis[now][next])continue;
        // b[next] = true;
        dfs_plan_1(next);
    }
}

void dfs(int now){//用于情况一的DFS，这里要回溯
    res[++cur] = now;//更新当前方案
    b[now] = true;
    int len = nei[now].size();
    for(int i = 0;i < len; i++){
        int next = nei[now][i];
        
        if(b[next])continue;
        //cout<<now<<" "<<next<<" "<<dis[i][next]<<endl;
        if(!dis[now][next])continue;
        // b[next] = true;
        //cout<<next;
        dfs(next);
        // b[next] = false;
    }
    b[now] = false;
    //cout<<"end."<<endl;
}

int main(){
//    freopen("input.txt", "r", stdin);
    init();//读入
    
    for(int i = 1; i <= n; i++) {
        //这里很巧妙，从小到大排列邻居，优化
        sort(nei[i].begin(), nei[i].end());
    }
    
    if(m == n - 1){//情况二
        dfs_plan_1(1);
        out();
        return 0;
    }

    //情况一

    Topo();//基环图

    for(int i = 1;i <= m; i++){//枚举删边
        int x = line[i].xx;
        int y = line[i].yy;

        if(use[x] || use[y])continue;//有一个点不在环中就跳过

        //cout<<i<<"line:"<<x<<" "<<y<<" "<<dis[x][y]<<endl;

        dis[x][y] = dis[y][x] = false;//删边
        cur = 0;

        dfs(1);//DFS

        work();//更新答案
        dis[x][y] = dis[y][x] = true;//恢复边
    }
    
    out();//输出
    return 0;
}

