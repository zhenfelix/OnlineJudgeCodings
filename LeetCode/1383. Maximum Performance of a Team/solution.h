// using ll = long long;

// const int MOD = 1e9+7;

// class Solution {
// public:
//     int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
//         vector<int> sidx(n), eidx(n);
//         vector<bool> used(n), candidate(n);
//         for (int i = 0; i < n; i++){
//             sidx[i] = i;
//             eidx[i] = i;
//         }
//         sort(sidx.begin(), sidx.end(), [&](int a, int b){
//             return speed[a] > speed[b];
//         });
//         sort(eidx.begin(), eidx.end(), [&](int a, int b){
//             return efficiency[a] < efficiency[b];
//         });
//         ll res = 0, cur = 0, cnt = 0, sums = 0;
//         for (int i = 0; i < n; i++){
//             int midx = eidx[i];
//             if (!candidate[midx]){
//                 candidate[midx] = true;
//                 cnt++; sums += speed[midx];
//             }
//             while (cur < n && cnt < k){
//                 if (!used[sidx[cur]] && !candidate[sidx[cur]]){
//                     candidate[sidx[cur]] = true;
//                     cnt++; sums += speed[sidx[cur]];
//                 }
//                 cur++;
//             }
//             res = max(res, sums*efficiency[midx]);
//             cnt--; sums -= speed[midx]; 
//             used[midx] = true;
//             candidate[midx] = false;
//         }
//         return res%MOD;

//     }
// };


class Solution {
public:
    int MOD=1000000007;
    int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
        vector<pair<int, int>> eng;
        for (int i=0; i<n; i++){
            eng.push_back(make_pair(efficiency[i], speed[i]));
        }
        sort(eng.begin(), eng.end());
        priority_queue<int, vector<int>, greater<int>> heap;
        int select = 0;
        long long sums = 0;
        long long ans=0;
        for (int i=n-1; i>=0; i--){
            heap.push(eng[i].second);
            sums = sums + eng[i].second;
            //cout<<sums<<endl;
            select = select+1;
            if (select>k){
                sums = sums-heap.top();
                //cout<<i<<" "<<heap.top()<<" "<<sums<<endl;
                select = select-1;
                heap.pop();
            }
            ans = max(ans, (long long)eng[i].first*sums);
        }
        return ans%MOD;
    }
};
