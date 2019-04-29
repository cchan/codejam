import sys
import random
def getresp(r, a):
    return sum(r[i] << (a // (i+1)) for i in range(len(r))) % (1 << 63)

print(1,2)
r = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)]
#r = [88, 99, 31, 92, 84, 80]
print(getresp(r, int(input())))
sys.stdout.flush()
print(getresp(r, int(input())))
sys.stdout.flush()
got = list(map(int, input().split(' ')))
if r == got:
    print(1)
    sys.stdout.flush()
    sys.stderr.write('success\n')
    exit(0)
else:
    print(-1)
    sys.stdout.flush()
    sys.stderr.write(str(r)+'\n'+str(got)+'\n')
    exit(1)
