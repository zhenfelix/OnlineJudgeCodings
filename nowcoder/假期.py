# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
company = list(map(int, input().split(' ')))
gym = list(map(int, input().split(' ')))


work, fit, relax = 0, 0, 0
for i in range(n):
    work, fit, relax = min(fit,relax) if company[i] == 1 else float('inf'), min(work,relax) if gym[i] == 1 else float('inf'), min(work,fit,relax) + 1

print(min(work,fit,relax))