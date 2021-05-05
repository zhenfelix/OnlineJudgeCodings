using LL = long long;
class Solution {
public:
    int magicTower(vector<int>& nums) {
        LL sum = 0;
        for(int x : nums) sum += x;
        if(sum < 0) return -1;
        sum = 0;
        priority_queue<int> pq;
        int ans = 0;
        for(int x : nums){
            if(x > 0) sum += x;
            else{
                sum += x;
                pq.push(-x);
                while(sum < 0){
                    sum += pq.top();
                    pq.pop();
                    ans += 1;
                }
            }
        }
        return ans;
    }
};
