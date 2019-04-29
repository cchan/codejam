# Find not nondecreasing/nonincreasing.
# Count direction changes. A change right after another doesn't count.
# Return this total minus one.

T = int(input())
for x in range(T):
    input()
    M = [int(s) for s in input().split(' ')]
    for i in range(len(M)):
        if M[i] < M[i+1]:
            up = True
            break
        elif M[i] > M[i+1]:
            up = False
            break
    lastchange = -1
    changes = 0
    for i in range(2, len(M)):
        if (up and M[i-1] > M[i]) or (not up and M[i-1] < M[i]):
            if lastchange != i - 1:
                changes += 1
                lastchange = i
            up = M[i-1] < M[i]
        if M[i-1] == M[i]:
            lastchange += 1
    print("Case #"+str(x+1)+": "+str(changes - 1))
