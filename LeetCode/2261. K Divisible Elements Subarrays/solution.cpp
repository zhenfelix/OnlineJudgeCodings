class Solution {
public:
int countDistinct(vector<int>& nums, int k, int p) {
    int cnt[201] = {}, hash[201] = {}, res = 0;
    for (int sz = 0; sz < nums.size(); ++sz) {
        unordered_map<int, vector<int>> s;
        auto collision = [&](const auto &ids, int i) {
            for (int j : ids)
                if (equal(begin(nums) + i, begin(nums) + i + sz + 1, begin(nums) + j))
                    return true;
            return false;
        };
        for (int i = 0; i + sz < nums.size(); ++i) {
            cnt[i] += nums[i + sz] % p == 0;
            if (cnt[i] <= k) {
                hash[i] = ((long long)hash[i] * 200 + nums[i + sz]) % 1000000007;
                if (!collision(s[hash[i]], i)) {
                    s[hash[i]].push_back(i);
                    ++res;
                }
            }
        }
    }
    return res;
}
};