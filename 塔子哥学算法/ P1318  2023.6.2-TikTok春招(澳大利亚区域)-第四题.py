
# 2023.6.2-TikTok春招(澳大利亚区域)-第四题
# 4.Resolve Conflicts in Calendar (Australia)

# You have received several meeting invitations in your calendar represented by an array meetings.The start and end time of each meeting invitation is indicated as meetings[i] =[starti,endi][starti​,endi​]. Find out the fewest number of meeting invitations to be rejected so that there is no conflicts of meetings in your calendar.

# ∣meetings∣≤105∣meetings∣≤105

# Example 1:

# Input

# 4
# 1 2
# 2 3
# 3 4
# 1 3

# Output:

# 1

# **Explanation: **

# Reject [1,3] to avoid the conflicts

# Example 2:

# Input

# 2
# 1 2
# 2 3

# Output:

# 0

# Explanation: You don't need to reject any meeting invitations

from heapq import *
n = int(input())
st = []
arr = []
for _ in range(n):
    a, b = list(map(int,input().split()))
    arr.append((a,b))
for a, b in sorted(arr):
    if st and st[-1] > a:
        if st[-1] > b:
            st.pop()
            st.append(b)
    else:
        st.append(b)
print(n-len(st))