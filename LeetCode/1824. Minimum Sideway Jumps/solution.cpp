// class Solution {
// public:
//     const int inf = 0x3f3f3f3f;
//     int minSideJumps(vector<int>& obstacles) {
//         vector<int> dp = {1,0,1};
//         int n = obstacles.size();
//         for (int i=1; i<n; ++i)
//         {
//             int op = obstacles[i];
//             vector<int> ndp = {inf,inf,inf};
//             if (op > 0) dp[op-1] = inf;
//             for (int p=0; p<3; ++p)
//             {
//                 if (p == op-1)
//                     continue;
//                 for (int q=0; q<3; ++q)
//                 {
//                     if (p == q)
//                         ndp[p] = min(ndp[p], dp[q]);
//                     else
//                         ndp[p] = min(ndp[p], dp[q]+1);
                    
//                 }
//             }
//             dp = std::move(ndp);
//         }
//         return *min_element(dp.begin(), dp.end());
//     }
// };

class Solution {
public:
    const int inf = 0x3f3f3f3f;
    int minSideJumps(vector<int>& obstacles) {
        vector<int> dp = {1,0,1};
        int n = obstacles.size();
        for (int i=1; i<n; ++i)
        {
            int op = obstacles[i];
            vector<int> ndp = std::move(dp);
            if (op > 0) ndp[op-1] = inf;
            int best = *min_element(ndp.begin(), ndp.end());
            for (int p=0; p<3; ++p)
            {
                if (p == op-1)
                    continue;
                ndp[p] = min(ndp[p], best+1);
            }
            dp = std::move(ndp);
        }
        return *min_element(dp.begin(), dp.end());
    }
};