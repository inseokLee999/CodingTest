import sys
input=sys.stdin.readline
N=int(input())
rs=[0,0,1,0,1,2,0,2,3,2]
add=[-1,0,1,0,1]
if N<=10:
    if(rs[N-1]==0):
        print(-1)
    else :
        print(rs[N-1])
else :
    print(((N//5)+1)+add[N%5])