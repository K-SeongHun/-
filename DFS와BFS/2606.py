import sys
N = int(sys.stdin.readline())
what = int(sys.stdin.readline())
com = [list(map(int, x.split())) for x in sys.stdin]
com.sort()
cnt = set([])

def ans(find):
    if (find == 1):
        for i in range(what):
            if com[i][0] == 1:
                cnt.add(com[i][1])
                ans(com[i][1])
    else:
        for i in range(what):
            if (com[i][0] == find):
                cnt.add(com[i][1])
                ans(com[i][1])
    return
ans(1)
print(len(cnt))
