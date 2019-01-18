// class Solution {
// public:
//     int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
//         int ans=0;
//         unordered_map<int,int> cd;
//         for(auto c: C){
//             for(auto d: D){
//                 cd[c+d]++;
//             }
//         }
//         for(auto a: A){
//             for(auto b: B){
//                 int target=-(a+b);
//                 if(cd.count(target))ans+=cd[target];
//             }
//         }
//         return ans;
//     }
// };


class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        // input is 4 tuples,
        // want to count pair, which is unique pair, so I will use unordered_set
        // separate problems into 2 sets of 2 tuples, and then working on them
        
        // build a map with <pair<int, int>, sum> for each 2 input sets.
        unordered_map<int, int> m;
        for (auto a: A) {
            for (auto b:B) {
                m[a+b]++;
            }
        }
        int ans = 0;
        for(auto c:C) {
            for (auto d:D) {
                int target = -(c+d);
                if (m.count(target))
                    ans += m[target];    
            }
        }
        
        return ans;
    }
};