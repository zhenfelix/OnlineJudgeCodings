
# 2023.6.2-TikTok春招(澳大利亚区域)-第五题
# 5. TikTok "Following" feed (Australia)

# Introduction One of the features TikTok is renown for is its video feeds. Users can seamlessly swipe through many videos with next to no loading time, and the recommendation algorithm will take care of ordering them judiciously. The "Following Page' is one of them, and shows videos from accounts that the user follows.

# Given n users identified by a unique id between 1 and n, a list of videos published by these users and a list of following/followed relationships, your task is to recreate each user's following' feed. Each feed is a list of at most 5 of the user's followed accounts' videos ordered by descending publication time (from newest to oldest). Note that some users may not follow anyone or not follow anyone who has posted a video, inwhich case their feed will be empty , in this case , you should ouput 'None'. lt is also possible that a user have published less than 5 videos, in which case their followers will see all of them.

# Example

# For instance, let's imagine:

# We have 4 users, n=4

# They've published the following videos. videos=[ [1, 10, 0],

# [1, 40,100],

# [2, 30, 200],

# [3, 20, 500],

# [3, 60, 1000],

# [4, 50, 750]]

# where every 3-dimensional array represents (user id, video id, publication timestamp).

# And the follower/followed relationships are:

# relationships = {

# ​ [1 , 2],

# ​ [3 , 2],

# ​ [3 , 1],

# ​ [2 , 1],

# ​ [3 , 4]

# }

# defined as [user id, followed account id]

# The answer will look ike this:

# User 1's feed is [30]

# User 2's feed is [40, 10]

# User 3's feed is [50,30,40,10] , This ls because user 3 follows users 2 and 1, which have published videos 50,30,40 and 10 sorted by publicaion time lin descending order (l.e.750,200,100,0)

# User 4's feed is [], because user 4 doesn't follow anyone, and thus their teed is empty.

# Functlon Descriptilon

# Complete the funcion buildFeeds 'in the editor below.

# Inputs

# buildFeeds has the following parameter(s): int numUsers: an integer representing the number of users with unique ids ranging from 1 to n int videosl[m][3]: an array of dimension m * 3 where each triple is (user id, video id,publication timestamp).

# Each video id and timestamp will appear only once.

# int relationships[k][2] : an array of dimension k * 2 where each double is (userA, userB) and means that userA follows userB.

# buildFeeds returns the following value: first line a integer: nn

# second line a integer: mm

# third line a integer: kk

# next mm lines:

# defined as [user id, followed account id] for every line , split by space.

# next kk lines:

# where each line is (userA, userB) split by sapce and means that userA follows userB.

# Output

# n lines, each line output is as follows: If the feed of user i is empty, output a string 'None'; otherwise output the feed of user i, and output the first 5 video ids in timestamp from newest to oldest; if the number of feeds is less than 5, output all video ids.

# Constraints

# 1≤n≤1001≤n≤100 1≤m≤1001≤m≤100 1≤k≤2001≤k≤200 Each video id is unique Each timestamp is unique
# Sample
# Sample Case 0

# Input

# 3
# 4
# 2
# 1 20 0
# 1 30 100
# 3 40 200
# 2 70 150
# 1 2
# 3 1

# Output

# 70
# None
# 30 20

# Sameple Case 1

# Input

# 4
# 6
# 5
# 1 10 0
# 1 40 100
# 2 30 200
# 3 20 500
# 3 60 1000
# 4 50 750
# 1 2
# 3 2
# 3 1
# 2 1
# 3 4

# Output

# 30
# 40 10
# 50 30 40 10
# None


n = int(input())
m = int(input())
k = int(input())
items = []
for _ in range(m):
    u, vid, t = list(map(int,input().split()))
    items.append((u-1,vid,t))
items.sort(key = lambda x : -x[-1])
followers = [set() for _ in range(n)]
for _ in range(k):
    a, b = list(map(int,input().split()))
    followers[b-1].add(a-1)
ans = [[] for _ in range(n)]
for u, vid, _ in items:
    tmp = []
    for f in followers[u]:
        if len(ans[f]) < 5: 
            tmp.append(f)
            ans[f].append(vid)
    followers[u] = tmp 
    # print(followers)
for i in range(n):
    if len(ans[i]) == 0:
        print("None")
    else:
        print(*ans[i])
