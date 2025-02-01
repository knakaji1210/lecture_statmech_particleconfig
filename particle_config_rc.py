# このプログラムはまだしっかりと実装できていない

import math

class pycolor:
    RED = '\033[31m'
    END = '\033[0m'
    
def arrangement(N, MaxLevel, Energy):
    if MaxLevel == 1:
        return [[N - Energy, Energy]]
    else:
        l = []
        Q = Energy // MaxLevel
        for q in range(Q + 1):
            r = arrangement(N - q, MaxLevel - 1, Energy - MaxLevel * q)
            for i in r:
                i.append(q)
            l.extend(r)
        return l

def print_arrangement(N, Energy):
    L = arrangement(N, Energy, Energy)
    W = [0] * len(L)
    for i in range(len(L)):
        f = 1
        for j in range(len(L[i])):
            f = f * math.factorial(L[i][j])
        W[i] = int(math.factorial(N) / f)
    for i in range(len(L)):
        if W[i] == max(W):
            print(L[i], " W = " + pycolor.RED + str(W[i]) + pycolor.END)
        else:
            print(L[i], " W = " + str(W[i]))
    print()
    print("Sum of W = " + str(sum(W)))
    print("Number of arrangement = " + str(len(L)))

print_arrangement(5, 5)