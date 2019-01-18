class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> st;
        
        vector<int> ans;
        for(int n: nums1){
            if(st.find(n)==st.end())st[n]=1;
            else st[n]++;
        }
        for(int m: nums2){
            if(st.find(m)!=st.end()&&st[m]>0){
                ans.push_back(m);
                st[m]--;
            }
        }
        return ans;
    }
};