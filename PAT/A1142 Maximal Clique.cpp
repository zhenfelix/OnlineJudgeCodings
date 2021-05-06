// #include <bits/stdc++.h>

// using namespace std;
// ofstream flog("log_solution");
// const int inf = 0x3f3f3f3f;


// int isClique(vector<set<int>> &graph, set<int> &vs, int nv){
//     for (const auto &v : vs){
//         for (const auto &nxt : vs){
//             if (nxt != v && graph[v].find(nxt) == graph[v].end())
//                 return 0;
//         }
//     }
//     for (int v = 1; v <= nv; v++){
//         if (vs.find(v) != vs.end())
//             continue;
//         bool found = true;
//         for (const auto &nxt : vs)
//         {
//             if (graph[v].find(nxt) == graph[v].end()){
//                 found = false;
//                 break;
//             }
//         }
//         if (found)
//             return 1;
//     }
//     return 2;

// }



// int main()
// {
//     ios::sync_with_stdio(false);
//     // freopen(input, "r", stdin);
//     // freopen(output, "w", stdout);
//     // freopen("input", "r", stdin);
//     int nv, nm, m, k;
//     cin >> nv >> nm;
//     vector<set<int>> graph(nv+1, set<int>());
    
//     while (nm--)
//     {
//         int a, b;
//         cin >> a >> b;
//         graph[a].insert(b);
//         graph[b].insert(a);
//     }
//     cin >> m;
//     while(m--){
//         cin >> k;
//         set<int> vs;
//         while (k--)
//         {
//             int x;
//             cin >> x;
//             vs.insert(x);
//         }
//         int res = isClique(graph, vs, nv);
//         if (res == 0){
//             cout << "Not a Clique\n";
//         }
//         else if (res == 1){
//             cout << "Not Maximal\n";
//         }
//         else{
//             cout << "Yes\n";
//         }
        
//     }
//     return 0;
// }



//18ms
#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;

int isClique(vector<vector<bool>> &graph, vector<bool> &vs, int nv)
{
    for (int v = 1; v <= nv; v++){
        if (!vs[v])
            continue;
        for (int nxt = 1; nxt <= nv; nxt++){
            if (vs[nxt] && nxt != v && !graph[v][nxt])
                return 0;
        }
    }
    for (int v = 1; v <= nv; v++){
        if (vs[v])
            continue;
        bool found = true;
        for (int nxt = 1; nxt <= nv; nxt++)
        {
            if (!vs[nxt])
                continue;
            if (!graph[v][nxt]){
                found = false;
                break;
            }
        }
        if (found)
            return 1;
    }
    return 2;
}

int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);
    int nv, nm, m, k;
    cin >> nv >> nm;
    vector<vector<bool>> graph(nv+1, vector<bool>(nv+1, false));

    while (nm--)
    {
        int a, b;
        cin >> a >> b;
        graph[a][b] = true;
        graph[b][a] = true;
    }
    cin >> m;
    while(m--){
        cin >> k;
        vector<bool> vs(nv+1, false);
        while (k--)
        {
            int x;
            cin >> x;
            vs[x] = true;
        }
        int res = isClique(graph, vs, nv);
        if (res == 0){
            cout << "Not a Clique\n";
        }
        else if (res == 1){
            cout << "Not Maximal\n";
        }
        else{
            cout << "Yes\n";
        }

    }
    return 0;
}














#include <bits/stdc++.h>
using namespace std;
int e[210][210];
int main() {
    int nv, ne, m, ta, tb, k;
    scanf("%d %d", &nv, &ne);
    for (int i = 0; i < ne; i++) {
        scanf("%d %d", &ta, &tb);
        e[ta][tb] = e[tb][ta] = 1;
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        scanf("%d", &k);
        vector<int> v(k);
        int hash[210] = {0}, isclique = 1, isMaximal = 1;
        for (int j = 0; j < k; j++) {
            scanf("%d", &v[j]);
            hash[v[j]] = 1;
        }
        for (int j = 0; j < k; j++) {
            if (isclique == 0) break;
            for (int l = j + 1; l < k; l++) {
                if (e[v[j]][v[l]] == 0) {
                    isclique = 0;
                    printf("Not a Clique\n");
                    break;
                }
            }
        }
        if (isclique == 0) continue;
        for (int j = 1; j <= nv; j++) {
            if (hash[j] == 0) {
                for (int l = 0; l < k; l++) {
                    if (e[v[l]][j] == 0) break;
                    if (l == k - 1) isMaximal = 0;
                }
            }
            if (isMaximal == 0) {
                printf("Not Maximal\n");
                break;
            }
        }
        if (isMaximal == 1) printf("Yes\n");
    }
    return 0;
}