using pii = pair<int,int>;
const int inf = 0x3f3f3f3f;

class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        vector<pii> intervals = {{inf,inf}};
        for (int i = 0; i <= n; i++)
            intervals.push_back({i-ranges[i],i+ranges[i]});
        sort(intervals.begin(), intervals.end());
        priority_queue<int,vector<int>> pq;
        int now = 0, cnt = 0;
        for (auto [s,e] : intervals){
            
            if (s > now){
                now = pq.top(); pq.pop();
                cnt++;
            }
            // cout << s << " " << e << " " << now << endl;
            if (now >= n)
                return cnt;
            if (s > now)
                return -1;
            pq.push(e);
        }
        return -1;
    }
};



using pii = pair<int,int>;
const int inf = 0x3f3f3f3f;

class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        vector<pii> intervals = {{inf,inf}};
        for (int i = 0; i <= n; i++)
            intervals.push_back({i-ranges[i],i+ranges[i]});
        sort(intervals.begin(), intervals.end());
        int reach = 0, now = 0, cnt = 0;
        for (auto [s,e] : intervals){
            
            if (s > now){
                now = reach;
                cnt++;
            }
            // cout << s << " " << e << " " << now << endl;
            if (now >= n)
                return cnt;
            if (s > now)
                return -1;
            reach = max(reach, e);
        }
        return -1;
    }
};