import random, sys


if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")
    t = sys.argv[1]
    random.seed(t)
    n, B = random.randint(1,1000), random.randint(1,100000)
    ts = [random.randint(1,100) for _ in range(n)]
    ps = [random.randint(1,10000) for _ in range(n)]
    print(n, B)
    print(*ts)
    print(*ps)