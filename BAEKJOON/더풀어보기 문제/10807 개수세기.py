import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
v=int(input())
cnt=0
for a in A:
    if a==v:
        cnt+=1
print(cnt)