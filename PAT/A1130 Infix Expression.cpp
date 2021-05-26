#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;

struct Node
{
    string data;
    int left, right;
};

istream &operator>>(istream &input, Node &node)
{
    input >> node.data >> node.left >> node.right;
}

string dfs(Node cur, vector<Node> &arr){
    if (cur.left == -1 && cur.right == -1){
        return cur.data;
    }
    string res;
    if (cur.left != -1){
        res += dfs(arr[cur.left], arr);
    }
    res += cur.data;
    if (cur.right != -1){
        res += dfs(arr[cur.right], arr);
    }
    return "("+res+")";
}

int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
//     freopen("input", "r", stdin);
    int n;
    cin >> n;
    vector<Node> arr(n+1);
    vector<int> parent(n+1, 0);
    for (int i = 1; i <= n; i++){
        cin >> arr[i];
        if (arr[i].left != -1){
            parent[arr[i].left] = i;
        }
        if (arr[i].right != -1){
            parent[arr[i].right] = i;
        }
    }
    Node root;
    for (int i = 1; i <= n; i++){
        if (parent[i] == 0){
            root = arr[i];
            break;
        }
    }
    string res = dfs(root, arr);
    if (res[0] == '(')
        res = res.substr(1,res.size()-2);
    cout << res << endl;
    return 0;
}
