// const string alphas = "abc";

// class Solution {
// public:
//     int n, rank;
//     void dfs(int idx, string &path){
//         // cout << idx << " " << path << endl;
//         if (idx == n){
//             rank--;
//             return;
//         }
//         if (rank == 0)
//             return;
//         for (auto ch : alphas){
//             if (!path.empty() && path.back()==ch)
//                 continue;
//             // cout << ch << endl;
//             path.push_back(ch);
//             dfs(idx+1, path);
//             if (rank == 0)
//                 return;
//             path.pop_back();
//         }
//         return;
//     }

//     string getHappyString(int n, int k) {
//         this->n = n;
//         this->rank = k;
//         string path = "";
//         dfs(0,path);
//         return path;
//     }
// };



vector<char> alphas = {'a','b','c'};
vector<vector<char>> mp = {{'b','c'},{'a','c'},{'a','b'}};

class Solution {
public:
    
    string getHappyString(int n, int k) {
        vector<int> pow(n,1);
        for (int i = 1; i < n; i++)
            pow[i] = pow[i-1]*2;
        if (k > 3*pow[n-1])
            return "";
        k--;
        string s;
        int idx = k/pow[n-1];
        s.push_back(alphas[idx]);
        k -= idx*pow[n-1];
        // cout << k << endl;
        for (int i = 1; i < n; i++){
            idx = ((k>>(n-i-1))&1);
            s.push_back(mp[s.back()-'a'][idx]);
        }
        return s;
    }
};