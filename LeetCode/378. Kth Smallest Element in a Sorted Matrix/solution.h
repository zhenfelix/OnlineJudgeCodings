// class Solution
// {
// public:
// 	int kthSmallest(vector<vector<int>>& matrix, int k)
// 	{
// 		int n = matrix.size();
// 		int le = matrix[0][0], ri = matrix[n - 1][n - 1];
// 		int mid = 0;
// 		while (le < ri)
// 		{
// 			mid = le + (ri-le)/2;
// 			int num = 0;
// 			for (int i = 0; i < n; i++)
// 			{
// 				int pos = upper_bound(matrix[i].begin(), matrix[i].end(), mid) - matrix[i].begin();
// 				num += pos;
// 			}
// 			if (num < k)
// 			{
// 				le = mid + 1;
// 			}
// 			else
// 			{
// 				ri = mid;
// 			}
// 		}
// 		return le;
// 	}
// };


// class Solution {
// public:
// struct compare
// {
//     bool operator()(const pair<int,pair<int, int> >& a, const pair<int,pair<int, int> >& b)
//     {
//         return a.first>b.first;
//     }
// };
//     int kthSmallest(vector<vector<int>>& arr, int k) {
        
//         int n=arr.size(),m=arr[0].size();
        
//         priority_queue< pair<int,pair<int, int> >, vector<pair<int, pair<int, int> > >, compare > p;
        
//         for(int i=0;i<n;i++)
//         p.push(make_pair(arr[i][0],make_pair(i,0)));
        
//         int x=k,ans;
//         while(x--)
//         {
//             int e=p.top().first;
//             int i=p.top().second.first;
//             int j=p.top().second.second;
//             ans=e;
//             p.pop();
//             if(j!=m-1)
//             p.push(make_pair(arr[i][j+1],make_pair(i,j+1)));
//         }
//         return ans;
        
//     }
// };


