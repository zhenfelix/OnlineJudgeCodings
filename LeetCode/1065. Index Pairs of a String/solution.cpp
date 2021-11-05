// class Solution {
// public:
//     vector<vector<int>> indexPairs(string text, vector<string>& words) {
//         set<string> dict;
//         for (auto w : words)
//             dict.insert(w);
//         vector<vector<int>> res;
//         int n = text.length();
//         for (int i = 0; i < n; i++){
//             for (int j = i; j < n && j-i+1 <= 50; j++){
//                 string s = text.substr(i,j-i+1);
//                 if (dict.count(s))
//                     res.push_back({i,j});
//             }
//         }
//         return res;
//     }
// };


class Solution {
public:
    vector<vector<int>> indexPairs(string text, vector<string>& words) {
        int n=words.size();
        vector<vector<int>>ans;
        for(int i=0;i<n;i++){
            string target=words[i];
            int j=0;
            int m=target.size();
            while(1){
                j=text.find(target,j);
                if(j!=-1){
                    ans.push_back({j,j+m-1});
                    j++;
                }else break;
            }
        }
        sort(ans.begin(),ans.end());
        return ans;
    }
};
