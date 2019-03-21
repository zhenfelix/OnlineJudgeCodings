class NumArray {
public:
    vector<int> sums;
    NumArray(vector<int> nums) {
        int tmp=0;
        sums.push_back(tmp);
        for(auto n: nums){
            tmp+=n;
            sums.push_back(tmp);
        }
    }
    
    int sumRange(int i, int j) {
        return sums[j+1]-sums[i];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */