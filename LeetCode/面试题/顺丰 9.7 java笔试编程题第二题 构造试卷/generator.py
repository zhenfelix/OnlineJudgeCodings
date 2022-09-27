import random, sys

seed = 2023245323

if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")
    t = sys.argv[1]
    random.seed(int(t)+seed)
    n = random.randint(1,2000)
    m = random.randint(1,n)
    arr = [random.randint(1,1000) for _ in range(n)]
    print(n,m)
    print(*arr)
