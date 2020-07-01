class Solution {
public:
    int minNumberOfSemesters(int n, vector<vector<int>>& dependencies, int k) {
        vector<int> pre(n);
        for(auto& e : dependencies){
            e[0] -= 1;
            e[1] -= 1;
            pre[e[1]] |= 1 << e[0];
        }
        vector<int> dp(1 << n, n);
        dp[0] = 0;
        for(int i = 0; i < (1 << n); i += 1){
            int ex = 0;
            for(int j = 0; j < n; j += 1) if((i & pre[j]) == pre[j]) ex |= 1 << j;
            ex &= ~i;
            for(int s = ex; s; s = (s - 1) & ex) if(__builtin_popcount(s) <= k){
                dp[i | s] = min(dp[i | s], dp[i] + 1);
            }
        }
        return dp.back();
    }
};

// class Solution {
//     struct Cmp {
//         bool operator() (const vector<int> &a, vector<int> &b) {
//             return a[1] < b[1];
//         }
//     };
    
//     int dfs(vector<vector<int>> &edges, vector<int> &depths, int idx) {
//         if (depths[idx] == -1) {
//             int depth = 0;
//             for (int e: edges[idx])
//                 depth = max(depth, dfs(edges, depths, e));
//             depths[idx] = depth + 1;
//         }
//         return depths[idx];
//     }
    
// public:
//     int minNumberOfSemesters(int n, vector<vector<int>>& dependencies, int k) {
//         vector<int> degrees(n);
//         vector<vector<int>> edges(n);
//         for (auto &dep: dependencies) {
//             degrees[dep[1]-1]++;
//             edges[dep[0]-1].push_back(dep[1]-1);
//         }
//         vector<int> depths(n, -1);
//         for (int i=0; i<n; i++)
//             dfs(edges, depths, i);  // compute depth for each node
        
//         priority_queue<vector<int>, vector<vector<int>>, Cmp> mqueue;  // priority_queue is based on depth of each node
//         for (int i=0; i<n; i++) {
//             if (degrees[i] == 0)
//                 mqueue.push({i, depths[i]});   // only put nodes that have indegree 0 in the priority_queue
//         }
        
//         int step = 0;
//         while (!mqueue.empty()) {
//             step++;
//             vector<vector<int>> next;
//             for (int i=0, j=mqueue.size(); i<k && j>0; i++, j--) {  // stop the current round when the queue is empty or "k" limit is reached
//                 vector<int> top = mqueue.top();
//                 mqueue.pop();
//                 for (int e: edges[top[0]]) {
//                     if (--degrees[e] == 0) {
//                      // note that, we can't simply put it in the priority_queue, otherwise it may be picked up in the current round
//                         next.push_back({e, depths[e]});
//                     }
//                 }
//             }
//             for (auto it: next)
//                 mqueue.push(it);
//         }
        
//         return step;
//     }
// };


class Solution {
public:
    int minNumberOfSemesters(int n, vector<vector<int>>& dep, int k) {
        vector<vector<int>> prereq(n);
        for(auto& d : dep) {
            prereq[d[1]-1].push_back(d[0]-1);
        }
        vector<vector<bool>> dp(n+1, vector<bool>(1 << n, false));
        dp[0][0] = true;
        queue<int> q;
        unordered_set<int> visited;
        int day = 0;
        q.push(0);
        visited.insert(0);
        while(!q.empty()){
            int len = q.size();
            for (int i = 0; i < len; ++i)
            {
                int cur = q.front();
                q.pop();
                if(cur == (1<<n)-1){
                    return day;
                }
                int nxtPossible = 0;
                for(int course = 0; course < n; course++) {
                    if(cur & (1 << course)) {
                        continue;
                    }
                    // can i take this course ?
                    bool ok = true;
                    for(int pre : prereq[course]) {
                        ok &= ((cur >> pre) & 1);
                    }
                    if(ok) {
                        nxtPossible |= (1<<course);
                    }
                }
                for(int take = nxtPossible; take; take = (take-1)&nxtPossible) {
                    // int nxtmask = (take & nxtPossible);
                    int takeCnt = __builtin_popcount(take);
                    if(takeCnt > k) {
                        continue;
                    }
                    if(visited.find(take|cur) != visited.end()){
                        continue;
                    }
                    q.push(take|cur);
                    visited.insert(take|cur);
                }
            }
            day += 1;

        }
        // for(int day = 0; day < n; day++) {
        //     for(int mask = 0; mask < (1 << n); mask++) {
        //         if(!dp[day][mask]) {
        //             continue;
        //         }
        //         dp[day+1][mask] = true;
        //         // vector<int> nxtPossible;
        //         int nxtPossible = 0;
        //         // where can i go from here
        //         for(int course = 0; course < n; course++) {
        //             if(mask & (1 << course)) {
        //                 continue;
        //             }
        //             // can i take this course ?
        //             bool ok = true;
        //             for(int pre : prereq[course]) {
        //                 ok &= ((mask >> pre) & 1);
        //             }
        //             if(ok) {
        //                 nxtPossible |= (1<<course);
        //             }
        //         }
        //         // printf("%d %d %d\n",day,mask,nxtPossible);
        //         // int NP = nxtPossible.size();
        //         for(int take = nxtPossible; take; take = (take-1)&nxtPossible) {
        //             // int nxtmask = (take & nxtPossible);
        //             int takeCnt = __builtin_popcount(take);
        //             if(takeCnt > k) {
        //                 continue;
        //             }
        //             dp[day+1][take|mask] = true;
        //         }
        //     }
        //     if(dp[day+1][(1 << n)-1]) {
        //         return day + 1;
        //     }
        // }
        assert(false);
    }
};

