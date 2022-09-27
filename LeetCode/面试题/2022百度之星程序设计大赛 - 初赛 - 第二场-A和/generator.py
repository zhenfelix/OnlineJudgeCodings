import random, sys

seed = 2023213

if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")
    t = sys.argv[1]
    random.seed(int(t)+seed)
    n, q, k = random.randint(1,10000), random.randint(1,1000), random.randint(3,10)
    arr = [random.randint(1,10000) for _ in range(n)]
    alpha = 1.8
    x = int((sum(arr)//n)*k*alpha)
    print(n,q,k,x)
    print(*arr)
    for _ in range(q):
        l, r = random.randint(1,n), random.randint(1,n)
        if l > r:
            l, r = r, l 
        print(l,r)