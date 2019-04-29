from fractions import gcd
T = int(input())
for i in range(T):
    input()
    c = [int(x) for x in input().split(' ')]
    primes = list()
    d = gcd(c[0], c[1])
    primes.append(c[0]//d)
    primes.append(d)
    for i in range(1, len(c)):
        d = c[i]//d
        primes.append(d)
    print(list(set(primes)))
    mapping = dict(zip(sorted(list(set(primes))), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    print(''.join([mapping[e] for e in primes]))
