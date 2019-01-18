#include<cstdio>
#include<queue>
using namespace std;
struct pixel{
	int x;
	int y;
	int z;
};
int m,n,l,t;
int sum,volumn=0;
bool mat[1300][130][65];
bool inq[1300][130][65]={false};
int dx[6],dy[6],dz[6];
queue<pixel>q;
void init(){
	int temp[6]={-1,1,0,0,0,0};
	for(int i=0;i<6;i++){
		dx[i]=temp[i%6];
		dy[i]=temp[(i+2)%6];
		dz[i]=temp[(i+4)%6];
	}
}
pixel set_adj(pixel x,int i){
	pixel ans;
	ans.x=x.x+dx[i];
	ans.y=x.y+dy[i];
	ans.z=x.z+dz[i];
	return ans;
}
bool judge(pixel a){
	int x,y,z;
	x=a.x,y=a.y,z=a.z;
	if(x<0||x>=m||y<0||y>=n||z<0||z>=l)return false;
	if(!mat[x][y][z]||inq[x][y][z])return false;
	return true;
}
void bfs(pixel s){
	sum=0;
	q.push(s);
	inq[s.x][s.y][s.z]=true;
	while(q.size()!=0){
		pixel front=q.front();
		q.pop();
		sum++;
		for(int i=0;i<6;i++){
			pixel adj=set_adj(front,i);
			if(judge(adj)){
				
				inq[adj.x][adj.y][adj.z]=true;
				q.push(adj);
			}
			
		}
		
	}
	
}
int main(){
	freopen("A1091.txt","r",stdin);
	init();
	int value;
	pixel source;
	scanf("%d%d%d%d",&m,&n,&l,&t);
	for(int k=0;k<l;k++)for(int i=0;i<m;i++)for(int j=0;j<n;j++){
		scanf("%d",&value);
		if(value==1)mat[i][j][k]=true;
		else mat[i][j][k]=false;
	}
	for(int i=0;i<m;i++)for(int j=0;j<n;j++)for(int k=0;k<l;k++){
		source.x=i;source.y=j;source.z=k;
		
		if(judge(source)){
			bfs(source);
			if(sum>=t)volumn+=sum;
			
		}
	}
	
	printf("%d",volumn);
	return 0;
}
