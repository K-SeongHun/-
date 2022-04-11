import sys
A, B, C = map(int, sys.stdin.readline().split())
if (A == B and B == C):
    print(10000 + A * 1000)
elif (A == B or B == C or A == C):
    print(1000 + (A if A == B else C) * 100)
else:
    print(max(A, B, C) * 100)
