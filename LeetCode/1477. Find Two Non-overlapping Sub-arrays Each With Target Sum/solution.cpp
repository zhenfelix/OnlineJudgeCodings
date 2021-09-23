// const int inf = 0x3f3f3f3f;
// class Solution {
// public:
//     int minSumOfLengths(vector<int>& arr, int target) {
//      int n = arr.size();
//      vector<int> left(n,inf), right(n,inf);
//      unordered_map<int,int> mp;
//      int sums = 0;
//      mp[0] = -1;
//      for (int i = 0; i < n; i++){
//          sums += arr[i];
//          if (mp.count(sums-target))
//              left[i] = i-mp[sums-target];
//          if (i > 0)
//              left[i] = min(left[i], left[i-1]);
//          mp[sums] = i;
//      }
//      sums = 0;
//      mp.clear();
//      mp[0] = n;
//      for (int i = n-1; i >= 0; i--){
//          sums += arr[i];
//          if (mp.count(sums-target))
//              right[i] = mp[sums-target]-i;
//          if (i < n-1)
//              right[i] = min(right[i], right[i+1]);
//          mp[sums] = i;
//      }
//      int res = inf;
//      for (int i = 1; i < n; i++){
//          res = min(res, left[i-1]+right[i]);
//      }
//      return res == inf ? -1 : res;

//     }
// };


// const int inf = 0x3f3f3f3f;
// class Solution {
// public:
//     int minSumOfLengths(vector<int>& arr, int target) {
//      int n = arr.size();
//      int res = inf;
//      vector<int> left(n,inf);
//      unordered_map<int,int> mp;
//      int sums = 0;
//      mp[0] = -1;
//      for (int i = 0; i < n; i++){
//          sums += arr[i];
//          if (mp.count(sums-target)){
//              if (mp[sums-target] >= 0)
//                  res = min(res, left[mp[sums-target]]+i-mp[sums-target]);
//              left[i] = i-mp[sums-target];
//          }
//          if (i > 0)
//              left[i] = min(left[i], left[i-1]);
//          mp[sums] = i;
//      }
//      return res == inf ? -1 : res;

//     }
// };



// const int inf = 0x3f3f3f3f;
class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        int n = arr.size();
        int res = inf;
        vector<int> dp(n,inf);
        int sums = 0, left = 0, right = 0;
        for (; right < n; right++){
            sums += arr[right];
            while (sums > target)
                sums -= arr[left++];
            if (sums == target){
                dp[right] = right-left+1;
                if (left > 0)
                    res = min(res, right-left+1+dp[left-1]);
            }
            if (right > 0)
                dp[right] = min(dp[right], dp[right-1]);
        }
        return res == inf ? -1 : res;

    }
};

// const int inf = 0x3f3f3f3f;
// const int maxn = 1e5+5;

// int dp[maxn];

// class Solution {
// public:
//     int minSumOfLengths(vector<int>& arr, int target) {
//      int n = arr.size();
//      int res = inf;
//      int sums = 0, left = 0, right = 0;
//      memset(dp, 0x3f, n*sizeof(int));
//      for (; right < n; right++){
//          sums += arr[right];
//          while (sums > target)
//              sums -= arr[left++];
//          if (sums == target){
//              dp[right] = right-left+1;
//              if (left > 0)
//                  res = min(res, right-left+1+dp[left-1]);
//          }
//          if (right > 0)
//              dp[right] = min(dp[right], dp[right-1]);
//      }
//      return res == inf ? -1 : res;

//     }
// };