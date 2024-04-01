"""
1. 아이디어
이중 for 문 -> 값이 1 && 방문 x -> bfs
bfs 돌면서 그림 개수 +1. 최대값 갱신
2. 시간복잡도
O(V+E)
V=MN
E=4V
3. 자료구조
그래프 전체 지도 int [][]
방문여부 : bool[][]
queue (Bfs)
"""
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
map=list(list(map(int,input().split()))for _ in range(n))
chk=[[False]*m for _ in range(n)]

def bfs(y,x):
for j in range(n):
    for i in range(m):
        if map[j][i]==1 and chk[j][i]==False:
            chk[j][i]=True
            cnt+=1