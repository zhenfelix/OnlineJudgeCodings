const int K = 10;

class Solution {
public:
    long long wonderfulSubstrings(string word) {
        int n = word.size();
        int state = 0;
        vector<int> cnt(1 << K);
        cnt[0] = 1;
        vector<int> good{0};
        for (int i = 0; i < K; ++i)
            good.emplace_back(1 << i);
        
        long long ans = 0;
        for (char c : word) {
            int t = 1 << (c - 'a');
            state ^= t;
            for (int g : good)
                ans += cnt[state ^ g];
            cnt[state]++;
        }
        
        return ans;
    }
};


作者：lucifer1004
链接：https://leetcode-cn.com/problems/number-of-wonderful-substrings/solution/zhuang-tai-ya-suo-qian-zhui-yi-huo-he-by-bgu9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。