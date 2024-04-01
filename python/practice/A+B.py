import sys
input = sys.stdin.readline

N,K=map(int,input().split())
S=list(map(int,input().strip()))
A=[]*K
B=[]*K
for i in range(K):
    a,b=map(int,input().strip())
    A.append(a)
    B.append(b)
print(A,B)