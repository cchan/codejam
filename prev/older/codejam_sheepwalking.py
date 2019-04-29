import sys
sys.setrecursionlimit(1010)

T = int(input())

memo = dict()
memo[(0,0)] = 0
memo[(0,1)] = memo[(1,0)] = 3
def solution(x, y):
  if (x,y) not in memo:
    if x == 0:
      memo[(x,y)] = solution(0, y-1)*2/3 + solution(1, y-1)/3 + 2
    elif y == 0:
      memo[(x,y)] = solution(x-1, 0)*2/3 + solution(x-1, 1)/3 + 2
    else:
      memo[(x,y)] = 1 + solution(x, y - 1) / 2 + solution(x - 1, y) / 2
  return memo[(x,y)]

for i in range(T):
  X, Y = [int(s) for s in input().split(' ')]
  print("Case #" + str(i+1) + ": " + str(solution(abs(X), abs(Y))))
