//TLE

using pii = pair<int,int>;

class Solution {
public:
    int getKth(int lo, int hi, int k) {
        priority_queue<pii,vector<pii>,greater<>> pq;
        int mx = 100000;
        vector<bool> visited(mx, false);
        visited[1] = true;
        pq.push({0,1});
        while (!pq.empty()){
            auto [step, cur] = pq.top(); pq.pop();
            // cout << step << " " << cur << endl;
            if (cur >= lo && cur <= hi){
                k--;
                // cout << k << " " << cur << endl;
            }
            if (k == 0)
                return cur;
            int nxt = cur*2;
            if (nxt < mx && !visited[nxt]){
                visited[nxt] = true;
                pq.push({step+1,nxt});
            }
            nxt = (cur-1)/3;
            if (cur == nxt*3+1 && (nxt&1) == 1 && nxt > 1 && !visited[nxt]){
                visited[nxt] = true;
                pq.push({step+1,nxt});
            }
        }
        return -1;
    }
};
