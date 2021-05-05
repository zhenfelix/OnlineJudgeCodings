#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");


struct Node{
    int val;
    Node *left = nullptr, *right = nullptr;
    Node() = default;
    Node(int x)
        : val(x), left(nullptr), right(nullptr)
        {}
};

struct BST
{
    Node* root = nullptr;
    BST() = default;
    Node* insert(int x, Node* cur){
        if (!cur){
            cur = new Node(x);
            return cur;
        }
        if (x <= cur->val){
            cur->left = insert(x, cur->left);
        }
        else{
            cur->right = insert(x, cur->right);
        }
        return cur;
    }
    void dfs(Node* cur, int d, map<int,int> &mp){
        if (!cur)
            return;
        mp[d]++;
        dfs(cur->left,d+1,mp);
        dfs(cur->right,d+1,mp);
    }
};




class Solution
{
public:
    void decode()
    {
        
    }
};



int main()
{
    // ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);

    
    Solution sol;
    int n, x;
    auto tree = BST();
    map<int,int> mp;
    
    cin >> n;
    while (n--)
    {
        cin >> x;
        tree.root = tree.insert(x, tree.root);
    }
    tree.dfs(tree.root,0,mp);
    int a = 0, b = 0;
    auto it = mp.rbegin();
    a = it->second;
    it++;
    if (it != mp.rend())
        b = it->second;
    cout << a << " + " << b << " = " << a+b << endl;
}