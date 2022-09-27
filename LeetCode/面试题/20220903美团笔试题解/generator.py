import random, sys

seed = 202324532321

if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")
    t = sys.argv[1]
    random.seed(int(t)+seed)
    n, m = random.randint(1,10), random.randint(1,10)
    k = random.randint(1,n)
    c = [random.randint(1,n) for _ in range(m)]
    a = [random.randint(1,10) for _ in range(m)]
    b = [random.randint(1,10) for _ in range(m)]
    print(n,m,k)
    print(*c)
    print(*a)
    print(*b)