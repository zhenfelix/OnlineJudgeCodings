import random, sys


if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")
    t = sys.argv[1]
    random.seed(t)
    n, k = random.randint(1,100000), random.randint(0,10)
    if n < k:
        n, k = k, n 
    print(n, k)