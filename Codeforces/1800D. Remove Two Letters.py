# D: Let f(i) be the string after removing s[i] and s[i+1], then f(i)==f(j) (i<j) is equivalent to s[t]==s[t+2] for all t in range [i, j-1]. Therefore, let the initial answer be n-1, and each t that s[t]==s[t+2] will contribute -1 to the answer.
for _ in range(int(input())):
    n=int(input())
    s=input()
    p=1
    for i in range(1,n-1):
        if s[i-1]!=s[i+1]:
            p+=1
    print(p)