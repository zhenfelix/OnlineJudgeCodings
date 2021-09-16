class Solution {
public:
    bool dfs(int i, vector<int> &arr, vector<bool> &seen, int n){
        if (i+1 == n*2)
            return true;
        if (arr[i] != 0)
            return dfs(i+1, arr, seen, n);
        for (int v = n; v >= 1; v--){
            if (!seen[v]){
                if (v > 1 && (i+v >= n*2-1 || arr[i+v] != 0))
                    continue;
                seen[v] = true;
                arr[i] = v;
                if (v > 1)
                    arr[i+v] = v;
                if (dfs(i+1,arr,seen,n))
                    return true;
                if (v > 1)
                    arr[i+v] = 0;
                arr[i] = 0;
                seen[v] = false;
            }
        }
        return false;
    }
    vector<int> constructDistancedSequence(int n) {
        vector<bool> seen(n+1,false);
        vector<int> arr(n*2-1,0);
        dfs(0,arr,seen,n);
        return arr;
    }
};