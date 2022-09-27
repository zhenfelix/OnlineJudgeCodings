import random, sys, os, time

def randgen(fn, kase) :
    os.system(f'python generator.py {kase} >' + fn)

def duipai(std, cur, kase):
    randgen('data.in', kase)
    s = f'case {kase}:'
    os.system('echo '+s+' >> logs')
    os.system('cat data.in >> logs')
    start = time.time()
    os.system('python ' + std + ' < data.in > data.ans')
    stop = time.time()
    start2 = time.time()
    os.system('python ' + cur + ' < data.in > data.out')
    # os.system('python ' + std + ' < data.in > data.out')
    stop2 = time.time()
    os.system('echo '+f'std timer: {stop-start}'+' >> logs')
    os.system('echo '+f'sol timer: {stop2-start2}'+' >> logs')
    if os.system('diff data.ans data.out'):
        print(f"Wrong on case {i}")
        return False 
    os.system('cat data.out >> logs')
    return True

N = 10
os.system('> logs')
for i in range(N):
    if not duipai('std.py', 'sol.py', i):
        break
    
