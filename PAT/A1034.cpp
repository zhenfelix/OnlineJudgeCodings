#include<iostream>
#include<string>
#include<map>
using namespace std;
#define nmax 2010
bool visit[nmax]={false};
int edge[nmax][nmax]={0},weight[nmax]={0};
int n,k,p,index=0;
map<string,int> str2int,gang;
map<int,string> int2str;

void dfs(int v,int &head,int &num,int &w){
	visit[v]=true;
	if(weight[v]>weight[head])head=v;
	num++;
	for(int i=0;i<p;i++){
		if(edge[v][i]>0){
			w+=edge[v][i];
			edge[v][i]=0;
			edge[i][v]=0;
			if(visit[i]==false){
				dfs(i,head,num,w);
			}
		}
	}
}
void dfs_main(){
	for(int i=0;i<p;i++){
		if(visit[i]==false){
			int head=i,num=0,w=0;
			dfs(i,head,num,w);
			if(num>2&&w>k){
				gang[int2str[head]]=num;
			}
		}
	}
}
void convert(string str){
	if(str2int.find(str)==str2int.end()){
		str2int[str]=index;
		int2str[index]=str;
		index++;
	}
}
int main(){
	freopen("A1034.txt","r",stdin);
	string str1,str2;
	int w,x,y;
	cin>>n>>k;
	for(int i=0;i<n;i++){
		cin>>str1>>str2>>w;
		convert(str1);
		convert(str2);
		x=str2int[str1];y=str2int[str2];
		edge[x][y]+=w;edge[y][x]+=w;
		weight[x]+=w;weight[y]+=w;
	}
	p=index;
	dfs_main();
	map<string,int>::iterator it;
	cout<<gang.size()<<endl;
	for(it=gang.begin();it!=gang.end();it++){
		cout<<it->first<<" "<<it->second<<endl;
	}
	return 0;
}
