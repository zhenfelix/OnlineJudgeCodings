# import sys
# sys.stdin = open("input.txt", "r")

s = input()
res, cnt = [''], []
for ch in s:
    if ch == '[':
        cnt.append('')
    elif ch == '|':
        cnt[-1] = int(cnt[-1])
        res.append('')
    elif ch == ']':
        tmp = res.pop()*cnt.pop()
        res[-1] = res[-1] + tmp
    elif ord('0') <= ord(ch) <= ord('9'):
        cnt[-1] = cnt[-1] + ch
    else:
        res[-1] = res[-1] + ch

print(res[0])

