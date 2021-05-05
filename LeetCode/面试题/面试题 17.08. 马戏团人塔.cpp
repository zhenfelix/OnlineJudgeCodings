// class Solution {
// public:
//     int lower_bound(vector<int> &candidates, int target){
//         int n = candidates.size();
//         int lo = 0, hi = n-1;
//         while (lo <= hi){
//             int mid = (lo+hi)/2;
//             if (candidates[mid] >= target)
//                 hi = mid - 1;
//             else
//                 lo = mid + 1;
//         }
//         return lo;
//     }
//     int bestSeqAtIndex(vector<int>& height, vector<int>& weight) {
//         int n = height.size();
//         vector<pair<int,int>> arr;
//         for (int i = 0; i < n; i++){
//             arr.push_back({height[i], -weight[i]});
//         }
//         sort(arr.begin(), arr.end());
//         vector<int> candidates;
//         for (auto [h, w] : arr){
//             int idx = lower_bound(candidates, -w);
//             if (idx == candidates.size())
//                 candidates.push_back(0);
//             candidates[idx] = -w;
//         }
//         return candidates.size();
//     }
// };


class Solution {
public:

    int bestSeqAtIndex(vector<int>& height, vector<int>& weight) {
        int n = height.size();
        vector<pair<int,int>> arr;
        for (int i = 0; i < n; i++){
            arr.push_back({height[i], -weight[i]});
        }
        sort(arr.begin(), arr.end());
        vector<int> candidates;
        for (auto [h, w] : arr){
            auto idx = lower_bound(candidates.begin(), candidates.end(), -w);
            if (idx == candidates.end())
                candidates.push_back(-w);
            else
                *idx = -w;
        }
        return candidates.size();
    }
};

// class Solution {
// public:
//     int bestSeqAtIndex(vector<int>& height, vector<int>& weight) {
//         vector<pair<int,int>> tmp;
//         for(int i = 0; i < height.size(); i++) tmp.push_back({height[i], weight[i]});
//         sort(tmp.begin(), tmp.end(), [](const pair<int,int> &a, const pair<int,int> &b) {
//             return a.first == b.first ? a.second > b.second : a.first < b.first;
//         });
//         vector<int> dp; //长度为N的地方 最小的数字
//         for(const auto &[h, w]: tmp) {
//             auto p = lower_bound(dp.begin(), dp.end(), w);  //二分查找第一个大于等于的地方
//             if(p == dp.end()) dp.push_back(w);
//             else *p = w;
//         }
//         return dp.size();
//     }
// };


