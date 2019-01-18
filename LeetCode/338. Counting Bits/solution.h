// class Solution {
// public:
//     vector<int> countBits(int num) {
//         vector<int> ans;
//         ans.push_back(0);
//         for(int i=1;i<=num;i++)ans.push_back(ans[i/2]+(i&1));
//         return ans;
//     }
// };

class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> ans(num+1,0);
        for(int i=1;i<=num;i++) {
           ans[i]=ans[i/2]+i%2;
        }
        return ans;
    }
};