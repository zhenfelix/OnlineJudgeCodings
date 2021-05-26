#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;

struct Node
{
    string address, nxt;
    int data;
    Node()
        : address("-2"), nxt("-1"), data(0)
        {}
    Node(string add_, string nxt_, int data_)
        : address(add_), nxt(nxt_), data(data_)
        {}
};


Node* append(Node *cur, Node *x){
    cur->nxt = (x ? x->address : "-1");
    return x;
}


int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
//     freopen("input", "r", stdin);
    string name;
    int n, k;
    cin >> name >> n >> k;
    string address, nxt;
    int data;
    Node *head;
    map<string,Node*> mp;
    mp.insert({"-1",nullptr});
    while (n--){
        cin >> address >> data >> nxt;
        mp[address] = new Node(address, nxt, data);
        if (address == name)
            head = mp[address];
    }
    
    Node *a = new Node(), *b = new Node(), *c = new Node();
    Node *cur_a = a, *cur_b = b, *cur_c = c;
    while (head)
    {
        if (head->data < 0){
            cur_a = append(cur_a, head);
        }
        else if (head->data <= k){
            cur_b = append(cur_b, head);
        }
        else{
            cur_c = append(cur_c, head);
        }
        head = mp[head->nxt];
    }
    append(cur_a, mp[b->nxt]);
    if (cur_b == b)
        cur_b = cur_a;
    append(cur_b, mp[c->nxt]);
    if (cur_c == c)
        cur_c = cur_b;
    append(cur_c, nullptr);
    head = mp[a->nxt];
    while (head)
    {
        cout << head->address << " " << head->data << " " << head->nxt << "\n";
        head = mp[head->nxt];
    }
    

    return 0;
}



// #include<cstdio>
// const int nmax=100010;
// struct Node{
// 	int data;
// 	int next;
// }node[nmax];
// int head,n,k,h1=-1,h2=-1,h3=-1,t1,t2,t3;
// void show(int h){
// 	int temp=h;
// 	while(temp!=-1){
// 		printf("%05d %d ",temp,node[temp].data);
// 		if(node[temp].next==-1)printf("-1\n");
// 		else printf("%05d\n",node[temp].next);
// 		temp=node[temp].next;
// 	}
// }
// int main(){
// 	//freopen("b.txt","r",stdin);
// 	scanf("%d%d%d",&head,&n,&k);
// 	for(int i=0;i<n;i++){
// 		int id;
// 		scanf("%d",&id);
// 		scanf("%d%d",&node[id].data,&node[id].next);
// 	}
// 	int temp=head;
// 	while(temp!=-1){
// 		int v=node[temp].data;
// 		int pn=node[temp].next;
// 		if(v<0){
// 			if(h1==-1){
// 				h1=temp;
// 				t1=temp;
// 			}
// 			else{
// 				node[t1].next=temp;
// 				t1=temp;
// 			}
// 			node[t1].next=-1;
// 		}
// 		else if(v>=0&&v<=k){
// 			if(h2==-1){
// 				h2=temp;
// 				t2=temp;
// 			}
// 			else{
// 				node[t2].next=temp;
// 				t2=temp;
// 			}
// 			node[t2].next=-1;
// 		}
// 		else{
// 			if(h3==-1){
// 				h3=temp;
// 				t3=temp;
// 			}
// 			else{
// 				node[t3].next=temp;
// 				t3=temp;
// 			}
// 			node[t3].next=-1;
// 		}
// 		temp=pn;
// 	}
// 	int option[]={h1,h2,h3};
// 	int tail[]={t1,t2,t3,-1};
// 	int t;
// 	head=-1;
// 	for(int i=0;i<3;i++){
// 		if(option[i]!=-1){
// 			if(head==-1){
// 				head=option[i];
// 			}
// 			else{
// 				node[t].next=option[i];
// 			}
// 			t=tail[i];
// 		}
// 	}
// 	show(head);

// 	return 0;
// }
