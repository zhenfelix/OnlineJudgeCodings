class Solution {
public:
    vector<int> ans;
    vector<int> ans0;
    Solution(vector<int> nums) {
        ans=nums;
        ans0=ans;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return ans0;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        int n=ans.size();
        
        generate(0,ans);
        return ans;
    }
    void generate(int idx, vector<int> &a){
        int n=a.size()-idx;
        if(n==0)return;
        swap(a[idx],a[idx+(rand()%n)]);
        generate(idx+1,a);
        return;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */