import sys
input = sys.stdin.readline
N=int(input())
M=int(input())
com=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    com[a].append(b)
    com[b].append(a)
cnt=0
visited=[False]*(N+1)
visited[1] = True
q=[]
q.append(1)
while q:
    u=q.pop()
    for v in com[u]:
        if not visited[v]:
            q.append(v)
            visited[v]=True
            cnt+=1
print(cnt)