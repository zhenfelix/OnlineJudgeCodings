import random, sys, os

def randgen(fn, kase) :
    os.system(f'python generator.py {kase} >' + fn)

def duipai(std, cur, kase):
    randgen('data.in', kase)
    s = f'case {kase}:'
    os.system('echo '+s+' >> logs')
    os.system('cat data.in >> logs')
    os.system('python ' + std + ' < data.in > data.ans')
    os.system('python ' + cur + ' < data.in > data.out')
    if os.system('diff data.ans data.out'):
        print(f"Wrong on case {i}")
        return False 
    os.system('cat data.out >> logs')
    return True

N = 50
os.system('> logs')
for i in range(N):
    if not duipai('std.py', 'sol.py', i):
        break
    
