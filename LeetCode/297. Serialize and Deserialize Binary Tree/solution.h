/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        queue<TreeNode*> q;
        string str="";
        q.push(root);
        while(!q.empty()){
            TreeNode* tmp=q.front();
            q.pop();
            if(tmp==NULL){
                str+="*/";
                continue;
            }
            str+=to_string(tmp->val);
            str+="/";
            q.push(tmp->left);
            q.push(tmp->right);
        }
        return str;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        queue<TreeNode*> q;
        TreeNode* root;
        int i=0;string tmp="";
        while(data[i]!='/'){
            tmp+=data[i];
            i++;
        }
        i++;
        if(tmp[0]=='*')root=NULL;
        else {
            root=new TreeNode(stoi(tmp));
            q.push(root);
        }
        while(i<data.length()){
            TreeNode *tmp=q.front();q.pop();
            string left="",right="";
            while(i<data.length()&&data[i]!='/'){
                left+=data[i];i++;
            }
            i++;
            if(left[0]=='*')tmp->left=NULL;
            else {
                tmp->left=new TreeNode(stoi(left));
                q.push(tmp->left);
            }
            while(i<data.length()&&data[i]!='/'){
                right+=data[i];i++;
            }
            i++;
            if(right[0]=='*')tmp->right=NULL;
            else {
                tmp->right=new TreeNode(stoi(right));
                q.push(tmp->right);
            }
        }
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));



//dfs

// class Codec {
// public:
//     // Encodes a tree to a single string.
//     string serialize(TreeNode* root) {
//         if (root == nullptr) return "#";
//         return to_string(root->val)+","+serialize(root->left)+","+serialize(root->right);
//     }

//     // Decodes your encoded data to tree.
//     TreeNode* deserialize(string data) {
//         return mydeserialize(data);
//     }
//     TreeNode* mydeserialize(string& data) {
//         if (data[0]=='#') {
//             if(data.size() > 1) data = data.substr(2);
//             return nullptr;
//         } else {
//             TreeNode* node = new TreeNode(helper(data));
//             node->left = mydeserialize(data);
//             node->right = mydeserialize(data);
//             return node;
//         }
//     }
// private:
//     int helper(string& data) {
//         int pos = data.find(',');
//         int val = stoi(data.substr(0,pos));
//         data = data.substr(pos+1);
//         return val;
//     }
// };