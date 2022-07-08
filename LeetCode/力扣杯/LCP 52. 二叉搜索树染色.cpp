/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
    set<int> st;

    void dfs(TreeNode *node) {
        if (node == nullptr) return;
        st.insert(node->val);
        dfs(node->left);
        dfs(node->right);
    }

public:
    int getNumber(TreeNode* root, vector<vector<int>>& ops) {
        dfs(root);
        int ans = 0;
        for (int i = (int) ops.size() - 1; i >= 0; i--) {
            // while (true) {
            //     auto it = st.lower_bound(ops[i][1]);
            //     if (it == st.end() || (*it) > ops[i][2]) break;
            //     st.erase(it);
            //     if (ops[i][0]) ans++;
            // }
            for (auto it = st.lower_bound(ops[i][1]); it != st.end() && (*it) <= ops[i][2];){
                st.erase(it++);
                if (ops[i][0]) ans++;
            }
        }
        return ans;
    }
};



// 作者：tsreaper
// 链接：https://leetcode-cn.com/problems/QO5KpG/solution/by-tsreaper-d64z/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




class Solution {
public:
    unordered_map<int, int> mp;
    vector<int> arr;
    int seg[100001 * 4];
    int lazy[100001 * 4];
    int getNumber(TreeNode* root, vector<vector<int>>& ops) {

        memset(lazy, -1, sizeof(lazy));
        dfs(root);

        int n = arr.size();
        for (int i = 0; i < n; i++) {
            mp[arr[i]] = i;
        }

        for (auto& op : ops) {
            int left = mp[op[1]];
            int right = mp[op[2]];
            if (op[0] == 0) {
                updateSeg(0, 0, n - 1, left, right, 0);

            }
            else {
                updateSeg(0, 0, n - 1, left, right, 1);
            }
        }

        return seg[0];
    }

    void updateSeg(int idx, int left, int right, int uleft, int uright, int val) {
        if (left > right || uright<left || uleft>right) return;

        if (uleft <= left && uright >= right) {
            seg[idx] = val*(right-left+1);
            lazy[idx] = val*(right-left+1);
            return;
        }

        int mid = (left + right) >> 1;

        if (lazy[idx] != -1) {
            int val = lazy[idx];
            int leftval = val == 0 ? 0 : (mid - left + 1);
            int rightval = val == 0 ? 0 : (right - mid);
            seg[idx * 2 + 1] = leftval;
            seg[idx * 2 + 2] = rightval;
            lazy[idx * 2 + 1] = leftval;
            lazy[idx * 2 + 2] = rightval;
            lazy[idx] = -1;
        }


        updateSeg(idx * 2 + 1, left, mid, uleft, uright, val);
        updateSeg(idx * 2 + 2, mid + 1, right, uleft, uright, val);
        seg[idx] = seg[idx * 2 + 1] + seg[idx * 2 + 2];
    }

    void dfs(TreeNode* root) {
        if (root == nullptr) return;

        dfs(root->left);
        arr.push_back(root->val);
        dfs(root->right);
    }
};

// feibilun