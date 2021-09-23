// 两个栈实现队列的方法

// 作者：hqztrue
// 链接：https://leetcode-cn.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/solution/zhen-zheng-de-onsuan-fa-c-48ms-100-by-hq-8puk/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



const int maxn = 1e5+5;
const int mask = (1<<21)-1;

int sl[maxn], sr[maxn];

class Solution {
public:
    int closestToTarget(vector<int>& arr, int target) {
        sl[0] = sr[0] = mask;
        int l = 0, r = 0, n = arr.size(), res = 1e8;
        for (int i = 0; i < n; i++){
            r++;
            sr[r] = (sr[r-1]&arr[i]);
            while ((sl[l]&sr[r]) < target){
                if (l == 0){
                    for (int j = 1; j <= r; j++){
                        sl[j] = (sl[j-1]&arr[i-j+1]);
                    }
                    l = r; r = 0;
                }
                l--;
            }
            res = min(res, (sl[l]&sr[r])-target);
            if (i-l-r >= 0)
                res = min(res, target-(sl[l]&sr[r]&arr[i-l-r]));
        }
        return res;
    }
};



// const int maxn = 21;
// const int inf = 0x3f3f3f3f;

// class Solution {
// public:
//     int closestToTarget(vector<int>& arr, int target) {
//         vector<vector<int>> bits(maxn);
//         int n = arr.size();
//         for (int i = n-1; i >= 0; i--){
//             int x = arr[i];
//             for (int j = 0; j < maxn; j++){
//                 if (((x>>j)&1) == 0)
//                     bits[j].push_back(i);
//             }
//         }
        
//         int res = inf;
//         for (int l = 0; l < n; l++){
//             vector<int> pos;
//             int x = arr[l];
//             for (int j = 0; j < maxn; j++){
//                 if (!bits[j].empty()){
//                     pos.push_back(bits[j].back());
//                     if (l == pos.back())
//                         bits[j].pop_back();
//                 }
//             }
//             sort(pos.begin(), pos.end());
//             for (auto r : pos){
//                 x &= arr[r];
//                 res = min(res, abs(target-x));
//             }
//         }
//         return res;
//     }
// };

class Solution {
public:
    int closestToTarget(vector<int>& arr, int target) {
        int ans = abs(arr[0] - target);
        vector<int> valid = {arr[0]};
        for (int num: arr) {
            vector<int> validNew = {num};
            ans = min(ans, abs(num - target));
            for (int prev: valid) {
                if ((prev&num) != validNew.back()){
                    validNew.push_back(prev & num);
                    ans = min(ans, abs((prev & num) - target));
                }
            }
            swap(valid, validNew);
        }
        return ans;
    }
};



// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/solution/zhao-dao-zui-jie-jin-mu-biao-zhi-de-han-shu-zhi-by/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。