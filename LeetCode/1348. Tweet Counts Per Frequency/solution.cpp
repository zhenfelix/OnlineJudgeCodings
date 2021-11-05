class TweetCounts {
public:
    TweetCounts() {}
    
    void recordTweet(string tweetName, int time) {
        record[tweetName][time]++;
    }
    
    vector<int> getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime) {
        int f = 1;
        f *= (freq == "minute") ? 60 : 1;
        f *= (freq == "hour") ? 60 * 60 : 1;
        f *= (freq == "day") ? 60 * 60 * 24 : 1;

        vector<int> ans;
        int t = startTime;
        while (t <= endTime) {
            auto bg = record[tweetName].lower_bound(t);
            auto ed = record[tweetName].upper_bound(min(t + f - 1, endTime));
            int cnt = 0;
            for (auto it = bg; it != ed; it++) {
                cnt += it->second;
            }
            ans.push_back(cnt);
            t += f;
        }
        return ans;
    }

private:
    unordered_map<string, map<int, int>> record;
};


// 作者：ikaruga
// 链接：https://leetcode-cn.com/problems/tweet-counts-per-frequency/solution/5334-by-ikaruga/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。