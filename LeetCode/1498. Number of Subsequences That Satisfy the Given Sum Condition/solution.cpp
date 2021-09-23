// using ll = long long;

// const int MOD = 1e9+7;
// const int maxn = 1e5+5;


// class Solution {
// public:
//     int quickmul(int a, int q){
//         int res = 1;
//         while (q){
//             if (q&1)
//                 res = ((ll)res*a)%MOD;
//             a = ((ll)a*a)%MOD;
//             q >>= 1;
//         }
//         return res;

//     }
//     int numSubseq(vector<int>& nums, int target) {
//         int n = nums.size();
//         sort(nums.begin(), nums.end());
//         int res = upper_bound(nums.begin(), nums.end(), target/2) - nums.begin();
//         for (int left = 0, right = n-1; left < right; left++){
//             while (left < right && nums[left]+nums[right] > target)
//                 right--;
//             res += quickmul(2,right-left)-1;
//             res %= MOD;
//         }
//         return res;
//     }
// };


using ll = long long;

const int MOD = 1e9+7;
const int maxn = 1e5+5;


class Solution {
public:
    int quickmul(int a, int q){
        if (q < 0)
            return 0;
        int res = 1;
        while (q){
            if (q&1)
                res = ((ll)res*a)%MOD;
            a = ((ll)a*a)%MOD;
            q >>= 1;
        }
        return res;

    }
    int numSubseq(vector<int>& nums, int target) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int res = 0;
        for (int left = 0, right = n-1; left <= right; left++){
            while (left <= right && nums[left]+nums[right] > target){
                right--;
                // cout << left << " " << right << endl;
            }
            res += quickmul(2,right-left);
            res %= MOD;
            // cout << left << " " << right << endl;
        }
        return res;
    }
};







using ll = long long;

const int MOD = 1e9+7;
const int maxn = 1e5+5;

int pow2[maxn];
bool initialized = false;


class Solution {
public:
    void init(){
        pow2[0] = 1;
        for (int i = 1; i < maxn; i++){
            pow2[i] = pow2[i-1]*2;
            pow2[i] %= MOD;
        }
        initialized = true;
    }
    int numSubseq(vector<int>& nums, int target) {
        if (!initialized)
            init();
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int res = 0;
        for (int left = 0, right = n-1; left <= right; left++){
            while (left <= right && nums[left]+nums[right] > target){
                right--;
            }
            if (right >= left){
                res += pow2[right-left];
                res %= MOD;
            }
        }
        return res;
    }
};