// class Solution {
// public:
//     int maxSatisfaction(vector<int>& satisfaction) {
//         sort(satisfaction.begin(), satisfaction.end());
//         int n = satisfaction.size();
//         int sums = 0;
//         for (int i = n-1; i >= 0; i--){
//             int cur = 0;
//             for (int j = i; j < n; j++){
//                 cur += satisfaction[j]*(j-i+1);
//             }
//             sums = max(sums, cur);
//         }
//         return sums;
//     }
// };

class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        sort(satisfaction.begin(), satisfaction.end());
        int n = satisfaction.size();
        int sums = 0, tot = 0;
        for (int i = n-1; i >= 0; i--){
            sums += satisfaction[i];
            if (sums < 0)
                break;
            tot += sums;
        }
        return tot;
    }
};