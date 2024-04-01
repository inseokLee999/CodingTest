"""
1. 아이디아
정점의 개수 V 간선의 개수 E
시작 k 로부터 i번 정점으로의 최단 경로값 출력
모든 점까지의 거리 초기값 INF
힙에서 하나씩 빼면서 수행 :
현재거리가 새로운 간선 걸칠 때보다 크면 갱신
새로운 거리 힙 추가
다익스트라
2. 시간 복잡도
다익스트라 O(ElgV)
3. 변수
heap[[비용, 다음 노드]]
edge=인접 리스트
dist[]=최단거리 어차피 시작점 k 는 정해져있으니 1차원 거리 배열 [INF]*V+1
"""
import heapq
import sys
input=sys.stdin.readline
V,E=map(int,input().split())
K=int(input())
edge=[[]*(V+1)]
for i in range(E):
    u,v,w=map(int,input().split())
    edge[u].append([w,v])
dist=[[]*(V+1) for _ in range(V+1)]
for i in range(V+1):
    for j in range(V+1):
        dist[i][i]=0