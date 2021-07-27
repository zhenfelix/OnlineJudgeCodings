class Solution {
public:
    int smallestChair(vector<vector<int>>& times, int targetFriend) {
        int n = times.size();
        priority_queue<int, vector<int>, greater<>> available;
        for (int i = 0; i < n; ++i)
            available.emplace(i);
        vector<tuple<int, int, int>> events;
        for (int i = 0; i < n; ++i) {
            events.emplace_back(times[i][1], -1, i);
            events.emplace_back(times[i][0], 1, i);
        }
        sort(events.begin(), events.end());
        vector<int> seats(n);
        
        for (auto [_time, event_type, idx] : events) {
            if (event_type == 1) {
                seats[idx] = available.top();
                if (idx == targetFriend)
                    return seats[idx];
                available.pop();
            } else {
                available.emplace(seats[idx]);
            }
        }
        
        return -1; // Should not return from here
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/pbqHVB/view/GZueTt/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。