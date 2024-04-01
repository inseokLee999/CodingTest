"""
1.아이디어
정점간에 최단거리를 출력
다익스트라
2. 시간 복잡도
다익스트라 O(ElgV)=10^6 *20
3.변수
dist[][]=int
인접 리스트 edge=
힙
"""
import heapq  
import sys
input = sys.stdin.readline
INF=sys.maxsize

N,M=map(int,input().split())
edge=[[] for _ in range(N+1)]
dist=[INF]*(N+1)
for i in range(M):
    u,v,w=map(int,input().split())
    edge[u].append([w,v])
X,Z=map(int,input().split())
dist[X]=0
heap=[[0,X]]
while heap:
    w,v=heapq.heappop(heap)
    if w!=dist[v]:continue
    for nw,nv in edge[v]:
        if dist[nv]>dist[v]+nw:
            dist[nv]=dist[v]+nw
            heapq.heappush(heap,(dist[nv],nv))
answer=dist[Z]
if answer==INF:print(-1)
else:print(answer)