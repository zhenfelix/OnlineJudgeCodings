# 题目内容

# 曾经有一个古老的城市，里面有一位聪明的工匠，他发明了一种特殊的双端队列。这个队列可以从头部或尾部添加数据，但是只能从头部移出数据。这个特殊的队列在城市里很受欢迎，人们用它来组织不同的任务。

# 有一天，城市里的塔子哥要用这个队列来完成一个非常重要的任务。他需要依次执行 2×n2×n 个指令，其中 nn 个指令是向队列中添加数据（可以从头部添加，也可以从尾部添加），依次添加 11 到 nn；另外 nn 个指令是从头部移出数据，但是要求移出的顺序为 11 到 nn 。

# 为了完成这个任务，塔子哥可以在任何时候调整队列中数据的顺序。但是，为了让移出数据的顺序正好是 11 到 nn，他需要知道最少需要调整几次。
# 输入描述

# 第一行一个整数 nn ，表示数据范围。

# 接下来有 2×n2×n 行，其中有 nn 行为添加数据：指令 head add x 表示从头部添加数据 xx ， tail add x 表示从尾部添加数据 xx ；

# 另外 nn 行为移出数据指令，指令为 remove 的形式，表示移出 11 个数据；

# 1≤n≤3×1051≤n≤3×105 。

# 所有的数据均合法。

# 注意：输入会保证按照1到n的顺序加入队列，确保输出时对应的的数据已经在队列中
# 输出描述

# 一个整数，表示塔子哥要调整的最小次数。
# 样例

# 输入

# 3
# head add 1
# remove
# tail add 2
# head add 3
# remove
# remove

# 输出

# 1

# 样例解释
# 输入命令    队列
# head add 1  1
# remove  
# tail add 2  2
# head add 3  3 2
# remove  2 3（调整一次）
#     3
# remove  

# 上述表格展示了所给用例的执行过程。

# 其中，第一次remove不需要调整，可以直接满足输出要求；

# 第二次remove命令执行时，需要调整队列中元素的位置，将2调整到最前面才可以满足输出的要求。

# 这个调整可以任何时候进行，可以调移成任何顺序。


# 小小的思维题，维护一下队列当前元素个数和是否有序。对于head add操作会让元素个数加一，且如果个数已经大于等于1了，会让队列无序；对于tail add操作会让元素个数加一；对于remove操作，如果此时无序就花费一次调整，元素个数减一。
n = int(input())
is_sorted = 1
res = 0
sz = 0
for i in range(n << 1):
    op = input().split()
    if op[0] == 'head':
        if sz >= 1:
            is_sorted = 0
        sz += 1
    if op[0] == 'tail':
        sz += 1
    if op[0] == 'remove':
        if not is_sorted:
            is_sorted = 1
            res += 1
        sz -= 1
print(res)



from collections import *
n = int(input())
q = deque()
left, right = -1, -1
cur = 1
ans = 0
for i in range(2*n):
    s = input().split()
   
    if len(s) == 1:
        x = q.popleft()
        if cur != x and x != left:
            ans += 1
            left = q[0]
            right = q[-1]
        elif left == x:
            if left != right  :
                left = q[0]
        cur += 1
    elif s[0] == "tail":
        v = int(s[-1])
        q.append(v)
    else:
        v = int(s[-1])
        q.appendleft(v)
print(ans)