#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;

void buildTree(int lo, int hi, vector<int> &arr, vector<int> &left, vector<int> &right){
    if (lo >= hi)
        return;
    int i = lo, k = arr.size();
    while (i <= hi && abs(arr[lo]) >= abs(arr[i]))
    {
        i++;
    }
    if (lo+1 < i)
        left[lo] = lo + 1;
    if (i <= hi)
        right[lo] = i;
    buildTree(lo+1,i-1,arr,left,right);
    buildTree(i,hi,arr,left,right);
    
}

tuple<bool,int,bool> dfs(int cur, vector<int> &arr, vector<int> &left, vector<int> &right){
    int k = arr.size();
    if (cur == k)
        return {true, 1, true};
    int cnt = (arr[cur] > 0 ? 1 : 0);
    bool isRB = true, isBlack = (arr[cur] > 0);
    int ll = left[cur], rr = right[cur];
    auto res_left = dfs(ll, arr, left, right);
    auto res_right = dfs(rr, arr, left, right);
    isRB &= std::get<0>(res_left);
    isRB &= std::get<0>(res_right);
    if (!isBlack){
        isRB &= std::get<2>(res_left);
        isRB &= std::get<2>(res_right);
    }
    isRB &= (std::get<1>(res_left) == std::get<1>(res_right));
    cnt += std::get<1>(res_left);
    return {isRB,cnt,isBlack};
}


int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);
    int k, n;
    cin >> n;
    while (n--)
    {
        cin >> k;
        vector<int> left(k,k), right(k,k), arr(k);
        for (int i = 0; i < k; i++)
            cin >> arr[i];
        buildTree(0, k-1, arr, left, right);
        auto result = dfs(0,arr,left,right);
        if (std::get<0>(result) && std::get<2>(result))
            cout << "Yes\n";
        else
            cout << "No\n";
    }
    
    return 0;
}










// #include<cstdio>
// #include<cmath>
// using namespace std;
// const int nmax=40;
// bool flag=true;
// struct Node{
// 	int data;
// 	int left,right;
// }node[nmax];
// void tree(int root,int end){
// 	int i=root+1;
// 	if(i>=end){
// 		node[root].left=-1;
// 		node[root].right=-1;
// 		return;
// 	}
// 	while(i<end){
// 		int temp=abs(node[i].data);
// 		if(temp>=abs(node[root].data))break;
// 		i++;
// 	}
// 	if(i>root+1){
// 		node[root].left=root+1;
//     	tree(node[root].left,i);
// 	}
// 	else{
// 		node[root].left=-1;
// 	}
// 	if(i<end){
// 		node[root].right=i;
//     	tree(node[root].right,end);  
// 	}
// 	else{
// 		node[root].right=-1;
// 	}
// 	return;
// }
// void preorder(int root,int pre){
// 	if(root==-1)return;
// 	if(pre<0&&node[root].data<0)flag=false;
// 	preorder(node[root].left,node[root].data);
// 	preorder(node[root].right,node[root].data);
// 	return;
// }
// int main(){
// 	//freopen("d.txt","r",stdin);
// 	int k,n;
// 	scanf("%d",&k);
	
// 	for(int i=0;i<k;i++){
// 		scanf("%d",&n);
// 		for(int j=0;j<n;j++){
// 			scanf("%d",&node[j].data);
// 		}
// 		tree(0,n);
// 		flag=true;
// 		preorder(0,-1);
// 		if(flag)printf("Yes\n");
// 		else printf("No\n");
		
// 	}
// }
