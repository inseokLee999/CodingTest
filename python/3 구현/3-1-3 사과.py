"""
1. 아이디어
한 번의 이동으로 사과를 먹을 수 있으면 1 없으면 0
이동했을때 1이면 1
0이거나 -1 이거나 out of range 이면 0
"""
import sys
input = sys.stdin.readline
A=list(list(map(int, input().split()))for _ in range(5))
r,c=map(int,input().split())
dy=[-1,0,1,0]
dx=[0,1,0,-1]
get_apple=False
for i in range(4):
    nr = r+dy[i]
    nc = c+dx[i]
    if 0<=nr<=4 and 0<=nc<=4 and A[nr][nc]==1:
        get_apple=True
        break
if get_apple==True:
    print(1)
else :
    print(0)

