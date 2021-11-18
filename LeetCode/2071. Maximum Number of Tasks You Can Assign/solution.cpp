class Solution {
public:
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int p, int strength) {
        int n = tasks.size(), m = workers.size();
        
        // Sorting the tasks and workers in increasing order
        sort(tasks.begin(), tasks.end());
        sort(workers.begin(), workers.end());
        int lo = 0, hi = min(m, n);
        int ans;
        
        while(lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int count = 0;
            bool flag = true;
            
            // Inserting all workers in a multiset
            multiset<int> st(workers.begin(), workers.end());
            
            // Checking if the mid smallest tasks can be assigned
            for(int i = mid - 1; i >= 0; i--) {
                
                // Case 1: Trying to assing to a worker without the pill
                auto it = prev(st.end());
                if(tasks[i] <= *it) {
                    
                    // Case 1 satisfied!
                    st.erase(it);
                } else {
                    
                    // Case 2: Trying to assign to a worker with the pill
                    auto it = st.lower_bound(tasks[i] - strength);
                    if(it != st.end()) {
                        
                        // Case 2 satisfied!
                        count++;
                        st.erase(it);
                    } else {
                        
                        // Case 3: Impossible to assign mid tasks
                        flag = false;
                        break;
                    }
                }
                
                // If at any moment, the number of pills require for mid tasks exceeds 
                // the allotted number of pills, we stop the loop
                if(count > p) {
                    flag = false;
                    break;
                }
            }
            
            if(flag) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return hi;
    }
};

// class Solution {
// public:
//     int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
//         int n = tasks.size(), m = workers.size();
        
//         sort(tasks.begin(), tasks.end());
//         sort(workers.begin(), workers.end());
        
//         auto check = [&](int k) {
//             if (m < k)
//                 return false;
            
//             multiset<int> ms(workers.rbegin(), workers.rbegin() + k);
//             int rem = pills;
//             for (int i = k - 1; i >= 0; --i) {
//                 // 贪心策略1
//                 auto it = ms.lower_bound(tasks[i]);
//                 if (it == ms.end()) {
//                     if (rem == 0)
//                         return false;
//                     it = ms.lower_bound(tasks[i] - strength);
//                     if (it == ms.end())
//                         return false;
//                     rem--;
//                     ms.erase(it);
//                 } else {
//                     ms.erase(it);
//                 }
                
//                 // 贪心策略2
//                 // if (rem) {
//                 //     auto it = ms.lower_bound(tasks[i] - strength);
//                 //     if (it == ms.end())
//                 //         return false;
//                 //     if (*it < tasks[i])
//                 //         rem--;
//                 //     ms.erase(it);
//                 // } else {
//                 //     auto it = ms.lower_bound(tasks[i]);
//                 //     if (it == ms.end())
//                 //         return false;
//                 //     ms.erase(it);
//                 // }
//             }
            
//             return true;
//         };
        
//         int lo = 1, hi = n;
//         while (lo <= hi) {
//             int mid = (lo + hi) >> 1;
                        
//             if (check(mid))
//                 lo = mid + 1;
//             else
//                 hi = mid - 1;
//         }
        
//         return hi;
//     }
// };


// // 作者：吴自华
// // 链接：https://leetcode-cn.com/circle/discuss/cj4dO9/view/Mwspom/
// // 来源：力扣（LeetCode）
// // 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。