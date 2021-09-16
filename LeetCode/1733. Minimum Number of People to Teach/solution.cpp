// bitset<505> speaks[505];

// class Solution {
// public:
//     int minimumTeachings(int n, vector<vector<int>>& languages, vector<vector<int>>& friendships) {
//         int m = languages.size();
//         for(int i = 0; i < m; i++){
//             speaks[i] = 0;
//             for (auto j : languages[i])
//                 speaks[i][j] = 1;
//         }
//         vector<pair<int,int>> todo;
//         for (auto f : friendships){
//             f[0]--;f[1]--;
//             if ((speaks[f[0]]&speaks[f[1]]) == 0)
//                 todo.push_back({f[0],f[1]});
//         }
//         int res = m;
//         for (int i = 1; i <= n; i++){
//             unordered_set<int> people;
//             for (auto [u,v] : todo){
//                 if(speaks[u][i] == 0)
//                     people.insert(u);
//                 if(speaks[v][i] == 0)
//                     people.insert(v);
//             }
//             res = min(res, (int) people.size());
//         }
//         return res;
//     }
// };

bitset<505> speaks[505], cnt[505];

class Solution {
public:
    int minimumTeachings(int n, vector<vector<int>>& languages, vector<vector<int>>& friendships) {
        int m = languages.size();
        for(int i = 0; i < m; i++){
            speaks[i] = 0;
            for (auto j : languages[i])
                speaks[i][j] = 1;
        }
        for (int i = 1; i <= n; i++)
            cnt[i] = 0;
        vector<pair<int,int>> todo;
        for (auto f : friendships){
            f[0]--;f[1]--;
            if ((speaks[f[0]]&speaks[f[1]]) == 0)
                for (int i = 1; i <= n; i++){
                    if(speaks[f[0]][i] == 0)
                        cnt[i][f[0]] = 1;
                    if(speaks[f[1]][i] == 0)
                        cnt[i][f[1]] = 1;
                }                
        }
        int res = m;
        for (int i = 1; i <= n; i++){
            res = min(res, (int)cnt[i].count());
        }
        
        return res;
    }
};