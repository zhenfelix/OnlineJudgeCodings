#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;

bool buildTree(int lo, int hi, vector<int> &preorder, int start, vector<int> &postorder, vector<int> &left, vector<int> &right)
{
    bool multiple = false;
    if (lo >= hi)
        return multiple;
    int i = start;
    for(; postorder[i] != preorder[lo+1]; i++);
    if (i-start == hi-lo-1)
        multiple = true;
    if (start <= i){
        left[lo] = lo+1;
        multiple |= buildTree(lo+1, lo+1+i-start, preorder, start, postorder, left, right);
    }
    if (lo+1+i+1-start <= hi){
        right[lo] = lo + 1 + i + 1 - start;
        multiple |= buildTree(lo + 1 + i + 1 - start, hi, preorder, i+1, postorder, left, right);
    }
    return multiple;
}

void dfs(int root, vector<int> &preorder, vector<int> &left, vector<int> &right, vector<int> &res){
    int n = preorder.size();
    int ll = left[root], rr = right[root];
    if (ll < n)
        dfs(ll, preorder, left, right, res);
    res.push_back(preorder[root]);
    if (rr < n)
        dfs(rr, preorder, left, right, res);
    

    
}


int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);
    int n;
    cin >> n;
    vector<int> left(n, n), right(n, n), preorder(n), postorder(n);
    for (int i = 0; i < n; i++)
        cin >> preorder[i];
    for (int i = 0; i < n; i++)
        cin >> postorder[i];
    bool multiple = buildTree(0, n - 1, preorder, 0, postorder, left, right);
    if (multiple)
        cout << "No\n";
    else 
        cout << "Yes\n";
    vector<int> res;
    dfs(0, preorder, left, right, res);
    for (int i = 0; i < n; i++)
    {
        if (i > 0)
            cout << " ";
        cout << res[i];
    }
    cout << endl;
    return 0;
}
