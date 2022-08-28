using pii = pair<int,int>;
class Solution {
public:
    int getLengthOfWaterfallFlow(int num, vector<int>& block) {
        priority_queue<pii, vector<pii>, greater<>> pq; 
        for (int i = 0; i < num; i++) pq.push({0,i});
        int ans = 0;
        for (auto b : block){
            auto [h, i] = pq.top(); pq.pop();
            pq.push({h+b,i});
            ans = max(ans, h+b);
        }
        return ans;
    }
};  