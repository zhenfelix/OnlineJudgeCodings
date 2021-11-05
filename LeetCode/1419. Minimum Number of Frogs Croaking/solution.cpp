    class Solution {
    public:
        int minNumberOfFrogs(string croakOfFrogs) {
            vector<int> mp(128), cnt(5,0);
            int res = 0;
            string str = "croak";
            for (int i = 0; i < str.length(); i++)
                mp[str[i]] = i+1;
            for (auto ch : croakOfFrogs){
                int s = mp[ch];
                cnt[s%5] += 1;
                cnt[s-1] -= 1;
                if (s-1 > 0 && cnt[s-1] < 0)
                    return -1;
                res = max(res, -cnt[0]);
            }
            return cnt[0] == 0 ? res : -1;
        }
    };