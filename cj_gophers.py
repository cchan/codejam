import sys

T,N,M = map(int, input().split(' '))

mods = dict()

for _ in range(T):
    for b in [2, 3, 5, 7, 11, 13, 17]:
        print(' '.join([str(b)]*18))
        sys.stdout.flush()
        mods[b] = sum(map(int, input().split(' '))) % b
    
    for i in range(1, M+1):
        for modulus, remainder in mods.items():
            if i % modulus != remainder:
                break
        else:
            print(i)
            sys.stdout.flush()
            if int(input()) == -1:
                exit()
            break
