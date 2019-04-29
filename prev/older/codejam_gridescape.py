def solution(K, R, C):
    if K >= 0 and K <= R*C:
        if K == R * C - 1:
            return "IMPOSSIBLE\n"
        else:
            rows = []
            for i in range(R):
                row = []
                for j in range(C):
                    if j == C - 1:
                        row.append("S")
                    elif i % 2 == 0:
                        row.append("E")
                    else:
                        row.append("W")
                rows.append(row)
            one_to_flip = R * C - K - 1
            if one_to_flip // C == 0:
              rows[one_to_flip // C][one_to_flip % C] = 'W'
            else:
              rows[one_to_flip // C][one_to_flip % C] = 'N'
            
            for i in range(R):
              if i % 2 == 1:
                rows[i] = reversed(rows[i])
            return "POSSIBLE\n" + '\n'.join(''.join(row) for row in rows)
    # EEEEEEES
    # SWWWWWWW
    # EEEEEEES

import sys
n = int(sys.stdin.readline())
for i in range(n):
    R, C, K = map(int, sys.stdin.readline().split(' '))
    sys.stdout.write("Case #" + str(i+1) + ": " + ''.join(solution(K, R, C)))
