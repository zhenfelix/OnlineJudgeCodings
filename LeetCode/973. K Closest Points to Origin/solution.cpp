// https://leetcode.com/problems/k-closest-points-to-origin/discuss/217966/c-3-lines-nth_element-on

// using pii = pair<int,int>;
// const int N = 10005;
// pii dists[N];

// class Solution {
// public:
//     vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
//         int n = points.size();
//         for (int i = 0; i < n; i++){
//             int x = points[i][0], y = points[i][1];
//             dists[i] = {x*x+y*y,i};
//         }
//         nth_element(dists, dists+k, dists+n);
//         vector<vector<int>> res;
//         for (int i = 0; i < k; i++){
//             int idx = dists[i].second;
//             res.push_back({points[idx][0], points[idx][1]});
//         }
//         return res;
//     }
// };


class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& a, int K) {
        nth_element(a.begin(),a.begin()+K,a.end(), [](auto&& l, auto&& r){return l[0]*l[0]+l[1]*l[1]<r[0]*r[0]+r[1]*r[1];});
        a.resize(K);
        return a;
    }
};
