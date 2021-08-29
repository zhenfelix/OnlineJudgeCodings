class Solution {
public:
    int minSupplyTimes(int num, int initWater, vector<vector<int>>& supplyStations) {
        priority_queue<int, vector<int>> pq;
        supplyStations.push_back({num,0});
        sort(supplyStations.begin(), supplyStations.end(), [](vector<int> &a, vector<int> &b){
            if (a[0] == b[0])
                return a[1] > b[1];
            return a[0] < b[0];
        });
        int reach = initWater, cnt = 0;
        for (auto &station : supplyStations){
            while (!pq.empty() && (reach < station[0])){
                reach += pq.top();
                cnt++;
                pq.pop();
            }
            // cout << reach << ' ' << station[0] << ' ' << station[1] << endl;
            if (reach >= num)
                return cnt;
            if (reach >= station[0])
                pq.push(station[1]);
            else
                return -1;
        }
        return -1;
    }
};