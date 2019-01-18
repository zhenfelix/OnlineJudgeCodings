#include<cstdio>
#include<algorithm>
using namespace std;
struct Cake{
	double weight;
	double sell;
	double price;
}c[1010];
bool cmp(Cake a,Cake b){
	return a.price>b.price;
}
int main(){
	freopen("B1020.txt","r",stdin);
	int N;
	double D,sum=0;
	scanf("%d%lf",&N,&D);
	for(int i=0;i<N;i++)scanf("%lf",&c[i].weight);
	for(int i=0;i<N;i++)scanf("%lf",&c[i].sell),c[i].price=c[i].sell/c[i].weight;
	sort(c,c+N,cmp);
	for(int i=0;i<N;i++){
		if(c[i].weight<D)sum+=c[i].sell,D-=c[i].weight;
		else {
			sum+=c[i].price*D;
			break;
		}
	}
	printf("%.2f",sum);
	return 0;
}
