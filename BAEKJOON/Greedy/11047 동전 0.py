import sys
input = sys.stdin.readline
N,K=map(int,input().split())
A=list(int(input().strip()) for _ in range(N))
cnt=0
while(K>0):
    for i in range(1,N+1):
        cnt+=K//A[N-i]
        K%=A[N-i]
print(cnt)