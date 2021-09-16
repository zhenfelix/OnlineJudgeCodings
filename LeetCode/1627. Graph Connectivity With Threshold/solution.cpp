// class Solution {
// public:
//     inline int gcd(int a, int b){
//         return b == 0 ? a : gcd(b, a%b);
//     }
//     vector<bool> areConnected(int n, int threshold, vector<vector<int>>& queries) {
//         vector<int> parent(n+1);
//         for (int i = 0; i <= n; i++)
//             parent[i] = i;
//         function<int(int)> find = [&](int root){
//             if (parent[root] != root)
//                 parent[root] = find(parent[root]);
//             return parent[root];
//         };
//         auto connect = [&](int a, int b){
//             int ra = find(a), rb = find(b);
//             if (ra != rb)
//                 parent[ra] = rb;
//         };
//         for (int i = 1; i <= n; i++){
//             for (int j = 1; j*j <= i; j++)
//                 if (i%j == 0){
//                     if (j > threshold)
//                         connect(i,j);
//                     if (i/j > threshold)
//                         connect(i,i/j);
//                 }
//         }
//         vector<bool> ans;
//         for (auto q : queries)
//             if (find(q[0]) != find(q[1]))
//                 ans.push_back(false);
//             else
//                 ans.push_back(true);
//         return ans;
//     }
// };

int p[10005];
class Solution {
public:
    int find(int x) {
        return x == p[x] ? p[x] : p[x] = find(p[x]);
    }
    vector<bool> areConnected(int n, int threshold, vector<vector<int>>& queries) {
        int m = queries.size();
        for (int i = 0; i <= n; i++) {
            p[i] = i;
        }
        for (int i = threshold + 1; i <= n; i++) {
            for (int j = i; j <= n; j += i) {
                p[find(j)] = find(i);
            }
        }
        vector<bool> res(m);
        for (int i = 0; i < m; i++) {
            int x = queries[i][0], y = queries[i][1];
            if (find(x) == find(y)) {
                res[i] = true;
            } else {
                res[i] = false;
            }
        }
        return res;
    }
};