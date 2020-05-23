def main():
    num = int(input())
    legal, illegal = [], []
    line = input().split(" ")
    for x in line:
        try:
            if -1000 <= float(x) <= 1000:
                if '.' in x:
                    if len(x) - x.find('.')-1 <= 2:
                        legal.append(float(x))
                    else:
                        illegal.append(x)
                else:
                    legal.append(float(x))
            else:
                illegal.append(x)
        except:
            illegal.append(x)
    for x in illegal:
        output = 'ERROR: {} is not a legal number'.format(x)
        print(output)
    if len(legal) == 0:
        output = 'The average of 0 numbers is Undefined'
    elif len(legal) == 1:
        ave = sum(legal) / len(legal)
        output = 'The average of {} number is {:.2f}'.format(len(legal), ave)
    else:
        ave = sum(legal) / len(legal)
        output = 'The average of {} numbers is {:.2f}'.format(len(legal), ave)
    print(output)
if __name__ =="__main__":
    main()



# import sys, heapq
# from collections import *


# sys.stdin = open('input.txt', 'r')
# n = int(input())
# s = input().split(' ')
# # print(s)
# nums = '0123456789'
# arr = []
# for ws in s:
#     # print(w)
#     flag = 1
#     w = ws.split('.')
#     if len(w) > 2:
#         print("ERROR: {} is not a legal number".format(ws))
#         continue
#     elif len(w) == 2:
#         a, b = w
#         if not a:
#             a = '0'
#     else:
#         a, b = w[0], '0'
#     if a and a[0] == '-':
#         flag = -1
#         a = a[1:]
#     if any(x not in nums for x in a+b) or len(b) > 2 or int(a) > 1000:
#         print("ERROR: {} is not a legal number".format(ws))
#     else:
#         arr.append(flag*(int(a)+int(b)/(10**len(b))))
# if len(arr) == 0:
#     print('The average of 0 numbers is Undefined')
# else:
#     res = sum(arr)/len(arr)

#     if len(arr) > 1:
#         print('The average of {} numbers is {:.2f}'.format(len(arr), res))
#     else:
#         print('The average of {} number is {:.2f}'.format(len(arr), res))