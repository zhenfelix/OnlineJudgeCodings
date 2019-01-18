#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <algorithm>
using namespace std;

void dfs(map<pair<int , int>, int> &line, map<int, vector<int>> &graph, map<int,bool> &visited, vector<pair<int, int>> &path, int &turn, vector<pair<int, int>> &tpath, int &tturn, int cur, int start, int target){
    
    if(cur==target){
        if(path.size()==0||tpath.size()<path.size()){
            path=tpath;turn=tturn;
        }
        else if(tpath.size()==path.size()&&tturn<turn){
            path=tpath;turn=tturn;
        }
        return;
    }
    
    for(auto x: graph[cur]){
        if(!visited[x]){
            visited[x]=true;
            if(cur!=start&&line[make_pair(cur, x)]!=line[tpath.back()])tturn++;
            tpath.push_back(make_pair(cur, x));
            dfs(line, graph, visited, path, turn, tpath, tturn, x, start, target);
            tpath.pop_back();
            if(cur!=start&&line[make_pair(cur, x)]!=line[tpath.back()])tturn--;
            visited[x]=false;
        }
    }
    return;
}


int main()
{
    freopen("input.txt","r",stdin);
    int n,m;
    map<pair<int , int>, int> line;
    map<int, vector<int>> graph;
    map<int,bool> visited;
    cin>>n;
    for (int i=0; i<n; i++) {
        cin>>m;
        vector<int> stops(m);
        for (int j=0; j<m; j++) {
            cin>>stops[j];
            visited[stops[j]]=false;
            if(j==0)continue;
            int a=stops[j-1],b=stops[j];
            graph[a].push_back(b);
            graph[b].push_back(a);
            line[make_pair(a, b)]=i+1;
            line[make_pair(b, a)]=i+1;
        }
    }
    int k;
    
    cin>>k;
    while (k--) {
        int a,b,turn=0,tturn=0;;
        vector<pair<int, int>> path,tpath;
        cin>>a>>b;
        visited[a]=true;
        dfs(line, graph, visited, path, turn, tpath, tturn, a, a, b);
        visited[a]=false;
        vector<int> ans,ans_line;
        ans.push_back(a);
        for (int i=0; i<path.size()-1; i++) {
            if(line[path[i]]!=line[path[i+1]]){
                ans.push_back(path[i].second);
                ans_line.push_back(line[path[i]]);
            }
        }
        ans.push_back(b);
        ans_line.push_back(line[path.back()]);
        cout<<path.size()<<endl;
        for(int i=0;i<ans.size()-1;i++)printf("Take Line#%d from %04d to %04d.\n",ans_line[i],ans[i],ans[i+1]);
//            cout<<"Take Line#"<<ans_line[i]<<" from "<<ans[i]<<" to "<<ans[i+1]<<"."<<endl;
        //format 0000!
    }
        
    return 0;
}

