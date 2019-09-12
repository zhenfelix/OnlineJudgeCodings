// 683. K Empty Slots




// class Solution {
// public:
//     // set<int>::iterator lower_bound(set<int> &st, int target){
//     //     set<int>::iterator it = st.begin();
//     //     int n = st.size();
//     //     int left = 0;
//     //     int right = n-1;
//     //     while(left <= right){
//     //         int mid = (left+right)/2;
//     //         if(*(it+mid) <= target){
//     //             left = mid + 1;
//     //         }
//     //         else{
//     //             right = mid - 1;
//     //         }
//     //     }
//     //     return it+left;
//     // }
//     int kEmptySlots(vector<int>& bulbs, int K) {
//         int n = bulbs.size();
//         if(n < 3 || K > n-2){
//             return -1;
//         }
//         set<int> idx;
//         idx.insert(-n);
//         idx.insert(2*n+1);
//         // printf("%d\n",idx.size());
//         for(int i=1;i<=n;i++){
//             set<int>::iterator it = idx.lower_bound(bulbs[i-1]);
//             int right = *it;
//             int left = *(--it);
//             // printf("%d,%d\n",left,right);
//             if(right-bulbs[i-1]-1 == K || bulbs[i-1]-left-1 == K){
//                 return i;
//             }
//             idx.insert(bulbs[i-1]);
//         }
//         return -1;
            
//     }
// };

class Solution {
public:
    int kEmptySlots(vector<int>& bulbs, int K) {
        set<int> on;
        for (int i = 0; i < bulbs.size(); ++i) {
            auto it = on.insert(bulbs[i]).first;
            if (it != on.begin()) {
                --it;
                if (bulbs[i] - *it == K + 1)
                    return i + 1;
                ++it;
            }
            ++it;
            if (it != on.end()) {
                if (*it - bulbs[i] == K + 1)
                    return i + 1;
            }
        }
        return -1;
    }
};



// class Solution {
// public:
//     int kEmptySlots(vector<int>& flowers, int k) {
//         int n = flowers.size();
//         if (n < 3 || k > n-2) return -1;
//         ++k;
//         int bs = n / k + 1;
//         vector<int> lows(bs, INT_MAX);
//         vector<int> highs(bs, INT_MIN);
//         for (int i = 0; i < n; ++i) {
//             int x = flowers[i] - 1;
//             int p = x / k;
//             if (x < lows[p]) {
//                 lows[p] = x;
//                 if (p > 0 && highs[p - 1] == x - k) return i + 1;
//             } 
//             if (x > highs[p]) {
//                 highs[p] = x;
//                 if (p < bs - 1 && lows[p + 1] == x + k) return i + 1;
//             }            
//         }
        
//         return -1;
//     }
// };