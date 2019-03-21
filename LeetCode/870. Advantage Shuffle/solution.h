// class Solution {
// public:
//     vector<int> advantageCount(vector<int>& A, vector<int>& B) {
//         int n=A.size();
//         vector<int> ans(n, 0);
//         sort(A.begin(), A.end());
//         for(int i=n-1;i>=0;i--){
//             int target=INT_MIN;
//             int idx=-1;
//             for(int j=0;j<n;j++){
//                 if(B[j]>target && B[j]<A[i]){
//                     idx=j;
//                     target=B[j];
//                 }
//             }
//             if(idx==-1)break;
//             ans[idx]=A[i];
//             B[idx]=INT_MIN;
//         }
//         int j=0;
//         for(int i=0;i<n;i++)if(B[i]!=INT_MIN)ans[i]=A[j++];
//         return ans;
//     }
// };


// class Solution {
// public:
//     vector<int> advantageCount(vector<int>& A, vector<int>& B) {
//         int n=A.size();
//         vector<int> ans(n, INT_MIN);
//         for(int i=0;i<n;i++){
//             int target=INT_MIN;
//             int idx=-1;
//             for(int j=0;j<n;j++){
//                 if(ans[j]==INT_MIN && B[j]>target && B[j]<A[i]){
//                     idx=j;
//                     target=B[j];
//                 }
//             }
//             if(idx!=-1){
//                 ans[idx]=A[i];
//             }
//             else{
//                 for(int j=0;j<n;j++){
//                 if(ans[j]==INT_MIN && B[j]>target){
//                     idx=j;
//                     target=B[j];
//                 }
//             }
//             ans[idx]=A[i];
//             }
//         }
//         return ans;
//     }
// };



class Solution {
public:
        vector<int> advantageCount(vector<int> A, vector<int> B) {
        map<int, int> m;
        for (int i : A) m[i]++;
        map<int,int>::iterator it;
        vector<int> res;
        for (int i : B) {
            it = m.upper_bound(i);
            int x = it != m.end() ? it->first : m.begin()->first;
            if (--m[x] == 0) m.erase(x);
            res.push_back(x);
        }
        return res;
    }
};