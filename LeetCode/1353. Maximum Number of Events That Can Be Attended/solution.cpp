const int inf = 0x3f3f3f3f;

class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        events.push_back({inf,inf});
        sort(events.begin(), events.end());
        priority_queue<int,vector<int>, greater<>> pq;
        int cnt = 0, now = 0;
        for (auto event : events){
            int start = event[0], finish = event[1];
            while (!pq.empty() && now < start){
                int t = pq.top(); pq.pop();
                if (t >= now){
                    now++;
                    cnt++;
                }
            }
            now = max(now, start);
            pq.push(finish);
        }
        return cnt;
    }
};