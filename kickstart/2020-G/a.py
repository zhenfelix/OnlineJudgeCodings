import sys
# sys.stdin = open("input.txt", "r")


def count(s):
    pre, res = 0, 0
    for i, ch in enumerate(s):
        if s[max(0,i-5+1):i+1] == "start":
            res += pre 
        if s[max(0,i-4+1):i+1] == "kick":
            pre += 1
    return res


n = int(input())
for i in range(n):
    s = input()
    cnt = count(s.lower())
    print("Case #{}: {}".format(i+1,cnt))

