"""
1. 아이디어
시작지점에서 1이 있는곳 까지 bfs
2. 시간복잡도
O(V+E)=
3. 자료구조
보드 int[][]
방문한 곳 bool[][]
거리 int[][]
bfs 큐
"""
from collections import deque
A = [list(map(int, input().split())) for _ in range(5)]
y, x = map(int, input().split())
chk = [[0]*5 for _ in range(5)]
dist = [[0]*5 for _ in range(5)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
q=deque()
def bfs(y,x):
    q.append((y,x))
    while q:
        ry,rx = q.popleft()
        if A[ry][rx]==1:
            return dist[ry][rx]
        for i in range(4):
            ny = ry+dy[i]
            nx = rx+dx[i]
            if 0<=ny<5 and 0<=nx<5 and A[ny][nx]!=-1 and chk[ny][nx]==0:
                chk[ny][nx]=1
                q.append((ny,nx))
                dist[ny][nx]=dist[ry][rx]+1
    return -1
for j in range(1,7):

chk[y][x]=1
print(bfs(y, x))