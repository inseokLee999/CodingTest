import sys
input = sys.stdin.readline
n,m=map(int,input().split())
A=list(map(int,input().split()))
B=list((int(input().strip()))for _ in range(m))

cnt=0
for b in B:
    cnt=0
    for a in A:
        if a>=b:
            cnt+=1
    print(cnt)
