class Solution {
public:
    int maxSumMinProduct(vector<int>& nums) {
        int n = nums.size();
        int MOD = 1000000007;
        vector<int> idx, left, right;
        vector<long long> presums;
        presums.push_back(0);
        for (int i = 0; i < n; i++){
            idx.push_back(i);
            left.push_back(i);
            right.push_back(i);
            presums.push_back(presums.back()+nums[i]);
        }
        sort(idx.begin(), idx.end(), [&](int a, int b){
            return nums[a] < nums[b];
        });
        vector<int> st;
        for (int i = 0; i < n; i++){
            while (!st.empty() && nums[st.back()] >= nums[i]){
                st.pop_back();
            }
            left[i] = st.empty() ? 0 : st.back()+1;
            st.push_back(i);
        }
        st.clear();
        for (int i = n-1; i >= 0; i--){
            while (!st.empty() && nums[st.back()] >= nums[i]){
                st.pop_back();
            }
            right[i] = st.empty() ? n-1 : st.back()-1;
            st.push_back(i);
        }
        long long res = 0;
        for (auto i : idx){
            res = max(res, nums[i]*(presums[right[i]+1]-presums[left[i]]));
        }
        return res%MOD;
    }
};



// using ll = long long;

// class Solution {
// public:
//     int maxSumMinProduct(vector<int>& nums) {
//         const int MOD = 1e9+7;
//         ll res = 0;
//         vector<ll> presums = {0};
//         map<int,vector<int>> mp;
//         int n = nums.size();
//         for (int i = 0; i < n; i++){
//             presums.push_back(presums.back()+nums[i]);
//             mp[nums[i]].push_back(i);
//         }
//         vector<int> left(n), right(n), parent(n);
//         for (int i = 0; i < n; i++){
//             left[i] = i;
//             right[i] = i;
//             parent[i] = i;
//         }
//         function<int(int)> find = [&](int root){
//             if (parent[root] != root)
//                 parent[root] = find(parent[root]);
//             return parent[root];
//         };
//         auto connect = [&](int u, int v){
//             if (nums[u] > nums[v])
//                 return false;
//             int ru = find(u), rv = find(v);
//             if (ru == rv)
//                 return false;
//             left[rv] = min(left[rv], left[ru]);
//             right[rv] = max(right[rv], right[ru]);
//             parent[ru] = rv;
//             return true;
//         };
//         for (auto it = mp.rbegin(); it != mp.rend(); it++){
//             auto &[k, vs] = *it;
//             for (auto i : vs){
//                 int r = i;
//                 while (r < n-1 && connect(r,r+1))
//                     r++;
//                 int l = i;
//                 while (l > 0 && connect(l,l-1))
//                     l--;
                
//             }
//             for (auto i : vs){
//                 i = find(i);
//                 int l = left[i], r = right[i];
//                 // cout << k << " " << l << " " << r << " " << presums[r+1]-presums[l] << endl;
//                 res = max(res, k*(presums[r+1]-presums[l]));
//             }
//         }
//         return res%MOD;
//     }
// };


class Solution {
public:
    int maxSumMinProduct(vector<int>& nums) {
        int n = nums.size();
        int MOD = 1000000007;
        vector<int> idx, left, right;
        vector<long long> presums;
        presums.push_back(0);
        for (int i = 0; i < n; i++){
            idx.push_back(i);
            left.push_back(i);
            right.push_back(i);
            presums.push_back(presums.back()+nums[i]);
        }
        sort(idx.begin(), idx.end(), [&](int a, int b){
            return nums[a] < nums[b];
        });
        vector<int> st;
        for (int i = 0; i < n; i++){
            while (!st.empty() && nums[st.back()] >= nums[i]){
                st.pop_back();
            }
            left[i] = st.empty() ? 0 : st.back()+1;
            st.push_back(i);
        }
        st.clear();
        for (int i = n-1; i >= 0; i--){
            while (!st.empty() && nums[st.back()] >= nums[i]){
                st.pop_back();
            }
            right[i] = st.empty() ? n-1 : st.back()-1;
            st.push_back(i);
        }
        long long res = 0;
        for (auto i : idx){
            res = max(res, nums[i]*(presums[right[i]+1]-presums[left[i]]));
        }
        return res%MOD;
    }
};