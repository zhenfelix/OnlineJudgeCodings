#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
//#include <pair>
using namespace std;

int main()
{
//    freopen("input.txt","r",stdin);
    int n,m,k,a,b;
    vector<pair<int, int>> edges;
    vector<int> colors;
    set<int> count;
    cin>>n>>m;
    for(int i=0;i<m;i++){cin>>a>>b;edges.push_back(make_pair(a, b));}
    cin>>k;
    while (k--) {
        bool flag=false;
        for (int i=0; i<n; i++) {
            int tmp; cin>>tmp; colors.push_back(tmp);
            count.insert(tmp);
        }
        for (auto x: edges) {
            if (colors[x.first]==colors[x.second]) {
                flag=true;
                break;
            }
        }
        if(flag)cout<<"No"<<endl;
        else cout<<count.size()<<"-coloring"<<endl;
        colors.clear();
        count.clear();
    }
    return 0;
}

auto __=[](){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();