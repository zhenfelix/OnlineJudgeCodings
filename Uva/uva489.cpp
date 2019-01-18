// UVa489 Hangman Judge
// Rujia Liu
// #include<stdio.h>
// #include<string.h>
// #define maxn 100
// int left, chance;
// char s[maxn], s2[maxn];
// int win, lose;

// void guess(char ch) {
//   int bad = 1;
//   for(int i = 0; i < strlen(s); i++)
//     if(s[i] == ch) { left--; s[i] = ' '; bad = 0; }
//   if(bad) --chance;
//   if(!chance) lose = 1;
//   if(!left) win = 1;
// }

// int main() {
//   freopen("UVa489.txt","r",stdin);
//   freopen("ans.txt","w",stdout);
//   int rnd;
//   while(scanf("%d%s%s", &rnd, s, s2) == 3 && rnd != -1) {
//     printf("Round %d\n", rnd);
//     win = lose = 0;
//     left = strlen(s);
//     chance = 7;
//     for(int i = 0; i < strlen(s2); i++) {
//       guess(s2[i]);
//       if(win || lose) break;
//     }
//     if(win) printf("You win.\n");
//     else if(lose) printf("You lose.\n");
//     else printf("You chickened out.\n");
//   }
//   return 0;
// }


#include<cstdio>
#include<cstring>
const int maxn=1000;
bool str[150];
char s[maxn];
int win,lose,left,chance;
void guess(char c){
  if(str[c])left--,str[c]=false;
  else chance--;
  if(!left)win=1;
  if(!chance)lose=1;
}
int main(){
  freopen("UVa489.txt","r",stdin);
  freopen("ans.txt","w",stdout);
  int rnd;
  while(scanf("%d\n",&rnd)!=EOF){
    if(rnd==-1)break;
    for(char i='a';i<='z';i++)str[i]=false;
    char c;
    left=0;
    while((c=getchar())!='\n'){
      if(!str[c])str[c]=true,left++;
    }
    win=0,lose=0,chance=7;
    scanf("%s\n",s);
    for(int i=0;i<strlen(s);i++){
      guess(s[i]);
      if(win||lose)break;
    }
    printf("Round %d\n",rnd);
    if(win)printf("You win.\n");
    else if(lose)printf("You lose.\n");
    else printf("You chickened out.\n");
  }
  return 0;
}