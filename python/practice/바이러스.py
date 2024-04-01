import sys
input = sys.stdin.readline
K,P,N=map(int,input().split())
remain=K
for i in range(N):
    remain=(remain*P)%1000000007
print(remain)