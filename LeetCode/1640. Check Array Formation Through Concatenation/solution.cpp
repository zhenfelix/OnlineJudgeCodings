// class Solution {
// public:
//     bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
//         int n = arr.size();
//         vector<int> mp(101,-1);
//         for (int i = 0; i < n; i++)
//             mp[arr[i]] = i;
//         for (auto piece : pieces){
//             int m = piece.size();
//             if (mp[piece[0]] == -1)
//                 return false;
//             for (int j = 1; j < m; j++){
//                 if (mp[piece[j]] == -1 || mp[piece[j]] != mp[piece[j-1]]+1)
//                     return false;
//             }
//         }
//         return true;
//     }
// };


class Solution {
public:
bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
    int p[101];
    memset(p, 0x7f, sizeof(p));
    for (int i = 0; i < arr.size(); i++)
        p[arr[i]] = i;

    for (auto piece : pieces) {
        int po = p[piece[0]];
        if (po == 0x7f7f7f7f)
            return false;

        for (int i = 1; i < piece.size(); i++) {
            if (po + i >= arr.size() || arr[po+i]!=piece[i])
                return false;
        }
    }
    return true;
}
};
