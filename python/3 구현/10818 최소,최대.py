import sys
input = sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
A.sort()
print(A[0],A[N-1])