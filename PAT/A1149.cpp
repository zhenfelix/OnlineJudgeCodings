// #include <iostream>
// #include <string>
// #include <cmath>
// #include <cstdio>
// #include <vector>
// #include <set>
// #include <unordered_set>
// #include <algorithm>
// //#include <pair>
// using namespace std;



// int main()
// {
//     freopen("input.txt","r",stdin);
//     int n,m;
//     unordered_set<long long> mp;
    
//     cin>>n>>m;
//     for(int i=0;i<n;i++){
//         long long a,b;
//         cin>>a>>b;
//         if(a>b)swap(a,b);
//         a=a*100000+b;
//         mp.insert(a);
//     }
//     for (int ii=0; ii<m; ii++) {
//         int k,len;
//         bool flag=false;
//         cin>>k;
//         vector<int> items(k);
//         for(int j=0;j<k;j++)cin>>items[j];
//         len=items.size();
//         sort(items.begin(), items.end());
//         for (int i=0; i<len-1; i++) {
//             for (int j=i+1; j<len; j++) {
//                 long long tmp=items[i]*100000+items[j];
//                 if(mp.find(tmp)!=mp.end()){
//                     flag=true;
//                     break;
//                 }
//             }
//             if(flag)break;
//         }
//         if(flag)cout<<"No"<<endl;
//         else cout<<"Yes"<<endl;
//     }

//     return 0;
// }

// time limit exceeded

#include <iostream>
#include <vector>
#include <map>
using namespace std;
int main() {
    int n, k, t1, t2;
    map<int,vector<int>> m;
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d%d", &t1, &t2);
        m[t1].push_back(t2);
        m[t2].push_back(t1);
    }
    while (k--) {
        int cnt, flag = 0, a[100000] = {0};
        scanf("%d", &cnt);
        vector<int> v(cnt);
        for (int i = 0; i < cnt; i++) {
            scanf("%d", &v[i]);
            a[v[i]] = 1;
        }
        for (int i = 0; i < v.size(); i++)
            for (int j = 0; j < m[v[i]].size(); j++)
                if (a[m[v[i]][j]] == 1) flag = 1;
        printf("%s\n",flag ? "No" :"Yes");
    }
    return 0;
}
