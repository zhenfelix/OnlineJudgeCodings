// class Solution {
// public:
//     void generate(int idx, vector<int> &nums, int n, vector<vector<int>> &ans){
//         if(idx==n)ans.push_back(nums);
//         for(int i=idx;i<n;i++){
//             swap(nums[idx],nums[i]);
//             generate(idx+1,nums,n,ans);
//             swap(nums[idx],nums[i]);
//         }
//         return;
//     }
//     vector<vector<int>> permute(vector<int>& nums) {
//         int n=nums.size();
//         vector<vector<int>> ans;
//         generate(0,nums,n,ans);
//         return ans;
//     }
// };


class Solution {
public:
    void recursion(vector<int> num, int i, int j, vector<vector<int> > &res) {
        if (i == j-1) {
            res.push_back(num);
            return;
        }
        for (int k = i; k < j; k++) {
            // if (i != k && num[i] == num[k]) continue;
            swap(num[i], num[k]);
            recursion(num, i+1, j, res);
        }
    }
    vector<vector<int> > permute(vector<int> &num) {
        // sort(num.begin(), num.end());
        vector<vector<int> >res;
        recursion(num, 0, num.size(), res);
        return res;
    }
};



class Solution {
public:
    void recursion(vector<int> &num, int i, int n, vector<vector<int> > &res) {
        if (i == n-1) {
            res.push_back(num);
            return;
        }
        for (int k = i; k < n; k++) {
            swap(num[i], num[k]);
            recursion(num, i+1, n, res);
            swap(num[i], num[k]);
        }
    }
    vector<vector<int> > permute(vector<int> &num) {
        vector<vector<int> >res;
        recursion(num, 0, num.size(), res);
        return res;
    }
};