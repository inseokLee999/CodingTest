import sys
input = sys.stdin.readline
N=int(input())
T=list(int(input().strip()) for _ in range(N))
rs=[1,1,2,4]
for i in range(4,max(T)+1):
    rs.append(rs[i-3]+rs[i-2]+rs[i-1])
for t in T:
    print(rs[t])