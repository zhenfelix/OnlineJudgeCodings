// #include<cstdio>
// #include<vector>
// using namespace std;
// const int nmax=10010;
// bool vs[nmax]={false};
// int G[nmax][2];

// int main(){
// 	//freopen("c.txt","r",stdin);
// 	int n,m,k,nv;
// 	scanf("%d%d",&n,&m);
// 	for(int i=0;i<m;i++){
// 		scanf("%d%d",&G[i][0],&G[i][1]);
// 	}
// 	scanf("%d",&k);
// 	for(int i=0;i<k;i++){
// 		scanf("%d",&nv);
// 		for(int j=0;j<nv;j++){
// 			int temp;
// 			scanf("%d",&temp);
// 			vs[temp]=true;
// 		}
// 		int j;
// 		for(j=0;j<m;j++){
// 			if(vs[G[j][0]]==false&&vs[G[j][1]]==false)break;
// 		}
// 		if(j<m)printf("No\n");
// 		else printf("Yes\n");
// 		for(int v=0;v<n;v++)vs[v]=false;
// 	}
// }


#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;




int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
//     freopen("input", "r", stdin);
    int n, m, k, len;
    cin >> n >> m;
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++){
        int a, b;
        cin >> a >> b;
        edges[i] = {a,b};
    }
    cin >> k;
    while (k--)
    {
        cin >> len;
        set<int> seen;
        bool flag = true;
        while (len--){
            int x;
            cin >> x;
            seen.insert(x);
        }
        for (auto item : edges){
            if (seen.find(item.first) == seen.end() && seen.find(item.second) == seen.end()){
                flag = false;
                break;
            }
        }
        if (flag)
        {
            cout << "Yes\n";
        }
        else
        {
            cout << "No\n";
        }
    }
    
    
    return 0;
}
