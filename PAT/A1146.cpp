#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
#include <unordered_set>
#include <algorithm>
//#include <pair>
using namespace std;



int main()
{
    freopen("input.txt","r",stdin);
    int n,m;
    cin>>n>>m;
    vector<vector<int>>edges(n+1,vector<int>(0));
    vector<int>indegree(n+1,0);
    vector<int> ans;
    while (m--) {
        int a,b;
        cin>>a>>b;
        edges[a].push_back(b);
        indegree[b]++;
    }
    int k;
    cin>>k;
    for (int id=0;id<k;id++) {
        int i=0,node;
        bool flag=false;
        vector<int> tmp=indegree;
        while(i<n){
            cin>>node;
//            if(tmp[node]!=0){flag=true;break;}//??? wrong answer// there are remaining node to read you cannot break
            if(tmp[node]!=0){flag=true;}
            for(auto x: edges[node])tmp[x]--;
            i++;
        }
        if(flag)ans.push_back(id);
    }
    for(int i=0;i<ans.size();i++){
        cout<<ans[i];
        if(i<ans.size()-1)cout<<" ";
    }
    cout<<endl;
    return 0;
}

