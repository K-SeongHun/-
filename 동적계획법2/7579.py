import sys

N, M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))
DP = [[0] * N for _ in range(N)]

