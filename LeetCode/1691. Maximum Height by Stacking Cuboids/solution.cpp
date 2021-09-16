class Solution {
public:
    int maxHeight(vector<vector<int>>& cuboids) {
        int n = cuboids.size();
        vector<tuple<int, int, int, int>> v;
        for (int i = 0; i < n; ++i) {
            const auto& cubic = cuboids[i];
            v.emplace_back(cubic[0], cubic[1], cubic[2], i);
            v.emplace_back(cubic[0], cubic[2], cubic[1], i);
            v.emplace_back(cubic[1], cubic[0], cubic[2], i);
            v.emplace_back(cubic[1], cubic[2], cubic[0], i);
            v.emplace_back(cubic[2], cubic[0], cubic[1], i);
            v.emplace_back(cubic[2], cubic[1], cubic[0], i);
        }
        
        sort(v.begin(), v.end());
        
        vector<int> f(n * 6);
        for (int i = 0; i < n * 6; ++i) {
            auto [wi, li, hi, idi] = v[i];
            for (int j = 0; j < i; ++j) {
                auto [wj, lj, hj, idj] = v[j];
                if (wj <= wi && lj <= li && hj <= hi && idj != idi) {
                    f[i] = max(f[i], f[j]);
                }
            }
            f[i] += hi;
        }
        
        return *max_element(f.begin(), f.end());
    }
};


// 作者：zerotrac2
// 链接：https://leetcode-cn.com/problems/maximum-height-by-stacking-cuboids/solution/dui-die-chang-fang-ti-de-zui-da-gao-du-b-qzgy/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

// class Solution {
// public:
//     int maxHeight(vector<vector<int>>& cuboids) {
//         int n = cuboids.size();
//         for (auto& cubic: cuboids) {
//             sort(cubic.begin(), cubic.end());
//         }
        
//         // 保证枚举关系拓扑性的排序都可以
//         // sort(cuboids.begin(), cuboids.end());
//         sort(cuboids.begin(), cuboids.end(), [](const auto& u, const auto& v) {
//             return u[2] + u[0] + u[1] < v[2] + v[0] + v[1];
//         });
        
//         vector<int> f(n);
//         for (int i = 0; i < n; ++i) {
//             for (int j = 0; j < i; ++j) {
//                 if (cuboids[j][0] <= cuboids[i][0] && cuboids[j][1] <= cuboids[i][1] && cuboids[j][2] <= cuboids[i][2]) {
//                     f[i] = max(f[i], f[j]);
//                 }
//             }
//             f[i] += cuboids[i][2];
//         }
        
//         return *max_element(f.begin(), f.end());
//     }
// };


// 作者：zerotrac2
// 链接：https://leetcode-cn.com/problems/maximum-height-by-stacking-cuboids/solution/dui-die-chang-fang-ti-de-zui-da-gao-du-b-qzgy/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。