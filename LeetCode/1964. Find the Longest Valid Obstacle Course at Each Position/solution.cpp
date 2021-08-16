class Solution {
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        int n = obstacles.size();
        vector<int> ans(n);
        vector<int> LIS;
        int i = 0;
        for (int obstacle : obstacles) {
            auto it = upper_bound(LIS.begin(), LIS.end(), obstacle);
            if (it == LIS.end()) {
                LIS.emplace_back(obstacle);
                ans[i] = LIS.size();
            } else {
                ans[i] = it - LIS.begin() + 1;
                *it = obstacle;
            }
            i++;
        }
        return ans;
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/avaR15/view/EIciXR/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。