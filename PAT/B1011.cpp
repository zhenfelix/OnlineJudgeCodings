#include<cstdio>
int main()
{
  int T,tcase=1;
  long long a,b,c;
  scanf("%d",&T);
  while(T--)
  {
    scanf("%lld%lld%lld",&a,&b,&c);
    if(a+b>c)printf("Case #%d: true\n",tcase++);
    else printf("Case #%d: false\n",tcase++);
  }
  return 0;
}
