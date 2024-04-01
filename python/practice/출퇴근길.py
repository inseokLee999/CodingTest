"""
1. 아이디어
출근길 S -> T 갈 수 있는 길 저장
퇴근길 T -> S 갈 수 있는 길 저장
S -> T 모든 경로 가면서 T가 되면 종료 이때 visited 를 들린 목록에 저장
집합으로 처리하면 갈수 있는 경로 저장가능
2. 시간 복잡도
O(V+E)= 3*10^5
3. 변수
경로 배열 int []*n
방문 목록 visited int[]
"""
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
route = []*n # n에서 연결된 간선
SetS=set()
SetT=set()
for i in range(m):
    x,y=map(int,input().split())
    route[x].append(y)
S,T=map(int,input().split())
visited=[0] * n
def reset():
    for i in range(n):
        visited[i]=0
    return
def find_route(S,T):
    can_visit=set()
    global route
    global visited
    q=[]
    q.append(S)
    while q:
        loc = q.pop()
        if loc==T:
            can_visit.add(for i in range(n))



