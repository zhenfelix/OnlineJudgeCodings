// class Solution {
// public:
//     vector<int> getRow(int rowIndex) {
//         vector<int> pre{1};
//         vector<int> cur=pre;
//         for(int i=0;i<rowIndex;i++){
//             for(int j=1;j<pre.size();j++)cur[j]=pre[j-1]+pre[j];
//             cur.push_back(1);
//             pre=cur;
//         }
//         return cur;
//     }
// };


class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> A(rowIndex+1, 0);
        A[0] = 1;
        for(int i=1; i<rowIndex+1; i++)
            for(int j=i; j>=1; j--)
                A[j] += A[j-1];
        return A;
    }
};