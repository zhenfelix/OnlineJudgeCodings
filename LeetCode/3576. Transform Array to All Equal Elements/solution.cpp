class Solution {
public:
    bool canMakeEqual(vector<int>& nums, int K) {
        int n = nums.size();

        // 所有值都变成 x 的最少操作次数
        auto check = [&](int x) {
            int cnt = 0;
            vector<int> vec = nums;
            // 从左到右考虑每个下标，如果不是目标值，必须操作
            for (int i = 0; i + 1 < n; i++) if (vec[i] != x) {
                vec[i] *= -1;
                vec[i + 1] *= -1;
                cnt++;
            }
            return vec[n - 1] == x && cnt <= K;
        };

        // 枚举最后变成 1 还是 -1
        return check(1) || check(-1);
    }
};