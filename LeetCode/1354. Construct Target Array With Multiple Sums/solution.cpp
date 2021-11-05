using ll = long long;
class Solution {
public:
    bool isPossible(vector<int>& target) {
        priority_queue<int,vector<int>> pq;
        ll sums = 0;
        for (auto x : target){
            sums += x;
            pq.push(x);
        }
        while (1){
            int a = pq.top(); pq.pop();
            int r = sums-a;
            if (r == 1 || a == 1)
                return true;
            // cout << a << " " << sums << endl;
            
            if (r == 0 || sums%r == 0 || sums%r == a)
                return false;
            pq.push(sums%r);
            sums = sums%r + r;
        }
        return true;

    }
};