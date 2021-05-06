#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;

void buildTree(int start, int lo, int hi, vector<int> &inorder, vector<int> &postorder, vector<int> &left, vector<int> &right)
{
    if (lo >= hi)
        return;
    int i = start;
    for(; inorder[i] != postorder[hi]; i++);
    if (start <= i-1){
        left[hi] = lo+i-1-start;
        buildTree(start, lo, lo+i-1-start, inorder, postorder, left, right);
    }
    if (lo+i-start < hi){
        right[hi] = hi-1;
        buildTree(i+1, lo+i-start, hi-1, inorder, postorder, left, right);
    }
    
}

void zigzag(int root, vector<int> &postorder, vector<int> &left, vector<int> &right){
    int n = postorder.size();
    vector<int> res, cur, nxt;
    bool flip = true;
    cur.push_back(root);
    while (!cur.empty()){
        if (flip){
            for (auto it = cur.rbegin(); it != cur.rend(); it++){
                res.push_back(postorder[*it]);
                if (right[*it] < n)
                    nxt.push_back(right[*it]);
                if (left[*it] < n)
                    nxt.push_back(left[*it]);
            }
            std::reverse(nxt.begin(), nxt.end());
        }
        else{
            for (auto it = cur.begin(); it != cur.end(); it++)
            {
                res.push_back(postorder[*it]);
                if (left[*it] < n)
                    nxt.push_back(left[*it]);
                if (right[*it] < n)
                    nxt.push_back(right[*it]);
            }
        }
        
        flip = !flip;
        std::swap(cur,nxt);
        nxt.clear();
    }
    for (int i = 0; i < n; i++){
        if (i > 0)
            cout << " ";
        cout << res[i]; 
    }
    cout << endl;

    
}


int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);
    int n;
    cin >> n;
    vector<int> left(n, n), right(n, n), postorder(n), inorder(n);
    for (int i = 0; i < n; i++)
        cin >> inorder[i];
    for (int i = 0; i < n; i++)
        cin >> postorder[i];
    buildTree(0, 0, n-1, inorder, postorder, left, right);
    zigzag(n-1, postorder, left, right);
    
    return 0;
}
