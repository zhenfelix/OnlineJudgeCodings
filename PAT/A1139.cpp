// #include<cstdio>
// #include<cmath>
// #include<algorithm>
// #include<map>
// using namespace std;
// const int nmax=310;
// map<int,int> mp,pm;
// bool G[nmax][nmax];
// struct Node{
// 	int x,y;
// }ans[100000];
// int n,m,k;
// bool cmp(Node a,Node b){
// 	if(a.x!=b.x)return a.x<b.x;
// 	else return a.y<b.y;
// }
// int main(){
// 	freopen("A1139.txt","r",stdin);
// 	int a,b,num=1;
// 	scanf("%d%d",&n,&m);
// 	for(int i=0;i<m;i++){
// 		scanf("%d%d",&a,&b);
// 		if(!mp[a]){
// 			mp[a]=num;
// 			pm[num]=a;
// 			num++;
// 		}
// 		if(!mp[b]){
// 			mp[b]=num;
// 			pm[num]=b;
// 			num++;
// 		}
// 		G[mp[a]][mp[b]]=true;
// 		G[mp[b]][mp[a]]=true;
// 	}
// 	scanf("%d",&k);
// 	int q;
// 	for(int i=0;i<k;i++){
// 		q=0;
// 		scanf("%d%d",&a,&b);
// 		for(int ii=1;ii<=n;ii++){
// 			for(int jj=1;jj<=n;jj++){
// 				if(G[mp[a]][ii]&&G[mp[b]][jj]&&G[ii][jj]&&a*pm[ii]>0&&b*pm[jj]>0){
// 						ans[q].x=abs(pm[ii]);ans[q].y=abs(pm[jj]);
// 				    	q++;
// 				}
// 			}
// 		}
// 		sort(ans,ans+q,cmp);
// 		printf("%d\n",q);
// 		for(int ii=0;ii<q;ii++)printf("%d %d\n",ans[ii].x,ans[ii].y);
// 	}
// 	return 0;
// }


// #include <iostream>
// #include <string>
// #include <cmath>
// #include <cstdio>
// #include <vector>
// #include <set>
// #include <map>
// #include <unordered_set>
// #include <algorithm>
// using namespace std;




// int main()
// {
//     freopen("input.txt","r",stdin);
//     int n,m;
//     cin>>n>>m;
//     map<int,vector<int>> fs;
//     map<pair<int , int>, bool> mp;
//     while (m--) {
//         int a,b;
//         cin>>a>>b;
//         fs[a].push_back(b);fs[b].push_back(a);
//         mp[make_pair(a , b)]=true;
//         mp[make_pair(b , a)]=true;
//     }
//     int k;
//     cin>>k;
//     while (k--) {
//         int a,b;
//         vector<pair<int , int>> ans;
//         cin>>a>>b;
//         for(auto x: fs[a]){
//             for(auto y: fs[b]){
//                 if(x!=b&&y!=a&&a*x>0&&b*y>0){// possible A [C A] B
//                     //1.是否考虑到-0000的情况 2.是否考虑到输出时候不足四位补0的 如0001 3.是否按照要求进行排序，A的朋友和B的朋友 4.是否考虑的环路的问题，如A C A B 思路： 枚举A的朋友C，枚举C的朋友D，枚举D的朋友找到B，他们的下标分别是a，i，j，b 通过判断性别和环路排除不符合的情况 tip： 1.可以将输入数据+9999将所有负数变为正数处理。
//                     pair<int, int> tmp1,tmp2;
//                     tmp1=make_pair(x, y);
//                     tmp2=make_pair(y, x);
//                 if(mp[tmp1]||mp[tmp2])ans.push_back(make_pair(abs(x), abs(y)));
                    
//                 }
//             }
//         }
//         cout<<ans.size()<<endl;
//         sort(ans.begin(), ans.end());
//         for(auto p: ans)printf("%04d %04d\n",p.first, p.second);//format 0000
//     }
    
    
//     return 0;
// }



#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");


struct Person{
    string id;
    bool male = true;
    bool operator==(const Person &other) const
    {
        return id == other.id;
    }
    bool operator!=(const Person &other) const
    {
        return !(id == other.id);
    }
    bool operator< (const Person& other) const
    {
        return id < other.id;
    }
};

istream &operator>> (istream &input, Person &cur)
{
    string tmp;
    input >> tmp;
    if (tmp[0] == '-')
    {
        cur.id = tmp.substr(1);
        cur.male = false;
    }
    else
    {
        cur.id = tmp;
    }

    return input;
}

// ostream& operator << (ostream& out, Person &cur){
//     out << (cur.male ? "male: " : "female: ") << cur.id;
//     return out;
// }

ostream &operator<<(ostream &out, Person &cur)
{
    out << cur.id;
    return out;
}

class Solution
{
public:
    void firstContact(Person a, Person b, set<pair<Person, Person>> &edges, map<Person, set<Person>> &graph)
    {
        vector<Person> fa, fb;
        for (auto &&p : graph[a]){
            if (a.male == p.male)
                fa.push_back(p);
        }
        for (auto &&p : graph[b]){
            if (b.male == p.male)
                fb.push_back(p);
        }
        vector<pair<Person,Person>> res;
        for (auto &&pa : fa){
            for (auto &&pb : fb){
                if (pa != b && pb != a && edges.find({pa,pb}) != edges.end())
                    res.push_back({pa,pb});
            }
        }
        sort(res.begin(), res.end());
        cout << res.size() << endl;
        for (auto &&p : res){
            // cout << p.first << " " << p.second << endl;
            printf("%s %s\n", p.first.id.c_str(), p.second.id.c_str());
        }
    }
};



int main()
{
    // ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);

    
    Solution sol;
    int n, m, k;
    set<pair<Person,Person>> edges;
    map<Person,set<Person>> graph;

    cin >> n >> m;
    while (m--)
    {
        Person a, b;
        cin >> a >> b;
        edges.insert({a, b});
        edges.insert({b, a});
        graph[a].insert(b);
        graph[b].insert(a);
        // cout << a << " " << b << endl;
    }
    cin >> k;
    while (k--){
        Person a, b;
        cin >> a >> b;
        sol.firstContact(a,b,edges,graph);
        // cout << a << " " << b << endl;//会超时
    }
}