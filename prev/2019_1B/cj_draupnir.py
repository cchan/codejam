import sys

T,W = map(int, input().split(' '))

mods = dict()

for _ in range(T):
    print(56)
    sys.stdout.flush()
    well1 = int(input()) # 56 28 18 14 11 9
    r1 = (well1 >> 56)
    r2 = (well1 >> 28) % 128
    
    print(150)
    sys.stdout.flush()
    well2 = int(input()) # 150 75 50 37 30 25
    r3 = (well2 >> 50)
    
    r4 = (well2 >> 37) % 128
    
    q1 = (well1 - (r1 << 56) - (r2 << 28) - (r3 << 18) - (r4 << 14)) >> 9 # = 4 x + y
    q2 = (well2 >> 25) % (1 << 12) # = 32 x + y
    r5 = (q2 - q1) // 28
    r6 = q1 - 4 * r5
    
    print(r1, r2, r3, r4, r5, r6)
    sys.stdout.flush()
    if int(input()) == -1:
        exit()
