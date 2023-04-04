t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mi = min(arr)
    if arr[0] == mi:
        print("Bob")
    else:
        print("Alice")

