#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;

struct Node
{
    int val, height;
    Node *left, *right;
    Node() = default;
    Node(int val_)
        : val(val_), height(1), left(nullptr), right(nullptr)
        {}
};

void updateHeight(Node *root){
    int h = 0;
    if (root->left)
        h = max(h, root->left->height);
    if (root->right)
        h = max(h, root->right->height);
    root->height = h+1;
}

Node* leftRotation(Node *root){
    Node *tmp = root->right;
    root->right = tmp->left;
    updateHeight(root);
    tmp->left = root;
    updateHeight(tmp);
    return tmp;
}

Node *rightRotation(Node *root)
{
    Node *tmp = root->left;
    root->left = tmp->right;
    updateHeight(root);
    tmp->right = root;
    updateHeight(tmp);
    return tmp;
}

int balanceFactor(Node *root){
    int left =  root->left ? root->left->height : 0;
    int right = root->right ? root->right->height : 0;
    return left-right;
}

Node *insert(Node *root, int val){
    if (!root){
        return new Node(val);
    }
    if (val > root->val){
        root->right = insert(root->right, val);
        updateHeight(root);
        if (balanceFactor(root) == -2){
            if (balanceFactor(root->right) == -1)
            {
                root = leftRotation(root);
            }
            else if (balanceFactor(root->right) == 1){
                root->right = rightRotation(root->right);
                root = leftRotation(root);
            }
        }
    }
    else{
        root->left = insert(root->left, val);
        updateHeight(root);
        if (balanceFactor(root) == 2)
        {
            if (balanceFactor(root->left) == 1)
            {
                root = rightRotation(root);
            }
            else if (balanceFactor(root->left) == -1)
            {
                root->left = leftRotation(root->left);
                root = rightRotation(root);
            }
        }
    }
    return root;

}

bool bfs(Node* root, vector<int> &res){
    bool flag = true;
    queue<pair<Node *, int>> q;
    q.push({root,0});
    while (!q.empty())
    {
        auto item = q.front(); q.pop();
        Node *cur = item.first;
        int idx = item.second;
        if (idx != res.size())
            flag = false;
        res.push_back(cur->val);
        if (cur->left)
            q.push({cur->left, idx*2+1});
        if (cur->right)
            q.push({cur->right, idx*2+2});
    }
    return flag;

}

int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
//     freopen("input", "r", stdin);
    int n, x;
    Node *root = nullptr;
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> x;
        root = insert(root, x);
    }
    vector<int> res;
    bool complete = bfs(root, res);
    for (int i = 0; i < n; i++)
    {
        if (i > 0)
            cout << " ";
        cout << res[i];
    }
    cout << "\n" << (complete ? "YES" : "NO") << endl;
    return 0;
}
